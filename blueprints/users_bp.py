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
def register():
    try:
        user_info = UserSchema(exclude=["id", "is_admin"]).load(request.json)
        
        user = User(
            email = user_info["email"],
            password = bcrypt.generate_password_hash(user_info["password"]).decode("utf8"),
            name = user_info.get("id", "name", "anonymous")
        )
        
        db.session.add(user)
        db.session.commit()
        
        return UserSchema(only=["email", "name"]).dump(user), 201
    except exc.IntegrityError:
        return {"error": "Email address already in use"}, 409


# Login a user and return a JWT key
@users_bp.route("/login", methods=["POST"])
def login():
    user_info = UserSchema(exclude=["id"]).load(request.json)
    
    stmt = db.select(User).where(User.email == user_info["email"])
    user = db.session.scalar(stmt)
    
    if user and bcrypt.check_password_hash(user.password, user_info["password"]):
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=100)) # To adjust timeout later
        return {"token": token, "user": UserSchema(only=["id", "email", "name"]).dump(user)}
    else:
        return {"error": "Invalid email or password"}, 401
    

# Get a single user
@users_bp.route("/<int:id>")
@jwt_required()
def one_user(id):
    
    stmt = db.select(User).filter_by(id = id)
    user = db.session.scalar(stmt)
    
    if user:
        authorize(user.user_id)
        return UserSchema(only=["id", "email", "name"]).dump(user)
    
    return {"error": "User not found"}, 404    
    
    
# Update a single user
@users_bp.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_user(id):
    
    user_info = UserSchema(exclude=["id"]).load(request.json)
    
    stmt = db.select(User).filter_by(id = id)
    user = db.session.scalar(stmt)
    
    if user:
        authorize(user.user_id)
        user.name = user_info.get("name", user.name)
        user.email = user_info.get("email", user.email)
        user.password = user_info.get("password", user.password)
        db.session.commit()
        return UserSchema().dump(user), 200
    
    return {"error": "User not found"}, 404   


# Delete a single user
@users_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    
    stmt = db.select(User).filter_by(id = id)
    user = db.session.scalar(stmt)
    
    if user:
        authorize(user.user_id)
        db.session.delete(user)
        db.session.commit()
        return {"status": f"{user.name} has been deleted"}, 200
    
    return {"error": "User not found"}, 404