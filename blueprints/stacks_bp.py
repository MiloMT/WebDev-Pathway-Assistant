from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.stack import Stack, StackSchema
from setup import db
from blueprints.stack_tools_bp import stack_tools_bp
from auth import authorize


stacks_bp = Blueprint("stacks", __name__, url_prefix="/stacks")
stacks_bp.register_blueprint(stack_tools_bp)


# Get all stacks
@stacks_bp.route("/")
def all_stacks():
    
    stmt = db.select(Stack).order_by("name")
    stacks = db.session.scalars(stmt).all()
    return StackSchema(many=True, exclude=["stack_tools"]).dump(stacks)


# Create a stack
@stacks_bp.route("/", methods=["POST"])
@jwt_required()
def create_stack():
    
    authorize()
    
    stack_info = StackSchema(exclude=["id"]).load(request.json)
    
    stack = Stack(
        name = stack_info["name"],
        description = stack_info.get("description", "")
    )
    
    db.session.add(stack)
    db.session.commit()
    
    return StackSchema(exclude=["stack_tools"]).dump(stack), 201


# Get a single stack
@stacks_bp.route("/<int:id>")
def one_stack(id):
    
    stmt = db.select(Stack).filter_by(id = id)
    stack = db.session.scalar(stmt)
    
    if stack:
        return StackSchema().dump(stack)
    
    return {"error": "Stack not found"}, 404


# Update a single stack
@stacks_bp.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_stack(id):
    
    authorize()
    
    stack_info = StackSchema(exclude=["id"]).load(request.json)
    
    stmt = db.select(Stack).filter_by(id = id)
    stack = db.session.scalar(stmt)
    
    if stack:
        stack.name = stack_info.get("name", stack.name)
        stack.description = stack_info.get("description", stack.description)
        db.session.commit()
        return StackSchema().dump(stack), 200
    
    return {"error": "Stack not found"}, 404   


# Delete a single stack
@stacks_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_stack(id):
    
    authorize()
    
    stmt = db.select(Stack).filter_by(id = id)
    stack = db.session.scalar(stmt)
    
    if stack:
        db.session.delete(stack)
        db.session.commit()
        return {"status": f"{stack.name} has been deleted"}, 200
    
    return {"error": "Stack not found"}, 404