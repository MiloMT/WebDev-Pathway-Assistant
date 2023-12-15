from flask import Blueprint, request
from auth import authorize
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta
from models.user import User, UserSchema
from blueprints.user_tools_bp import user_tools_bp
# from blueprints.user_plans_bp import user_plans_bp
from setup import bcrypt, db
from sqlalchemy import exc


users_bp = Blueprint("users", __name__, url_prefix="/users")
users_bp.register_blueprint(user_tools_bp)
# users_bp.register_blueprint(user_plans_bp)

# Get all users
@users_bp.route("/")
@jwt_required()
def all_users():
    
    authorize()
    
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True, exclude=["password", "user_tools"]).dump(users)


# Register a new user
@users_bp.route("/", methods=["POST"])
def create_user():
    
    user_info = UserSchema(exclude=["id", "is_admin"]).load(request.json)
    
    user = User(
        email = user_info["email"],
        password = bcrypt.generate_password_hash(user_info["password"]).decode("utf8"),
        name = user_info["name"]
    )
    
    try:   
        db.session.add(user)
        db.session.commit()
    except exc.IntegrityError:
        return {"error": "Email address already in use"}, 409 
    
    return UserSchema(only=["id", "email", "name"]).dump(user), 201
    


# Login a user and return a JWT key
@users_bp.route("/login", methods=["POST"])
def login():
    user_info = UserSchema(exclude=["id"]).load(request.json, partial=True)
    
    stmt = db.select(User).where(User.email == user_info["email"])
    user = db.session.scalar(stmt)
    
    if user and bcrypt.check_password_hash(user.password, user_info["password"]):
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
        return {"token": token, "user": UserSchema(only=["id", "email", "name"]).dump(user)}
    else:
        return {"error": "Invalid email or password"}, 401
    

# Get a single user
@users_bp.route("/<int:user_id>")
@jwt_required()
def get_user(user_id):
    
    stmt = db.select(User).filter_by(id = user_id)
    user = db.session.scalar(stmt)
    
    if user:
        authorize(user.id)
        return UserSchema(only=["id", "email", "name"]).dump(user)
    
    return {"error": "User not found"}, 404    
    
    
# Update a single user
@users_bp.route("/<int:user_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_user(user_id):
    
    user_info = UserSchema(exclude=["id"]).load(request.json)
    
    stmt = db.select(User).filter_by(id = user_id)
    user = db.session.scalar(stmt)
    
    if user:
        authorize(user.id)
        user.name = user_info.get("name", user.name)
        user.email = user_info.get("email", user.email)
        user.password = bcrypt.generate_password_hash(user_info.get("password", user.password)).decode("utf8")
        if "is_admin" in user_info:
            authorize()
            user.is_admin = user_info["is_admin"]
        try:
            db.session.commit()
        except exc.IntegrityError:
            return {"error": "Email address already in use"}, 409 
        
        if "is_admin" in user_info:
            return UserSchema(exclude=["user_tools", "password"]).dump(user), 200
        else:
            return UserSchema(exclude=["user_tools", "password", "is_admin"]).dump(user), 200
    
    return {"error": "User not found"}, 404   


# Delete a single user
@users_bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    
    stmt = db.select(User).filter_by(id = user_id)
    user = db.session.scalar(stmt)
    
    if user:
        authorize(user.id)
        try:
            db.session.delete(user)
            db.session.commit()
        except (exc.IntegrityError, AssertionError):
            return {"error": "This user is linked to other resources. Dependencies must be removed first."}, 409
        
        return {"status": f"{user.name} has been deleted"}, 200
    
    return {"error": "User not found"}, 404