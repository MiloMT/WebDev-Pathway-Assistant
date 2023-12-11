from flask import Blueprint, request
# from flask_jwt_extended import jwt_required, get_jwt_identity
from models.stack import Stack, StackSchema
from models.stack_tool import Stack_Tool, Stack_ToolSchema
from setup import db
# from auth import authorize


stack_tools_bp = Blueprint("stack_tools", __name__, url_prefix="/<int:stack_id>/tools")


# Get all stack tools
@stack_tools_bp.route("/")
# @jwt_required()
def all_stack_tools(stack_id):
    
    stmt = db.select(Stack).filter_by(id = stack_id)
    stack = db.session.scalar(stmt)
    
    if stack:
        return Stack_ToolSchema(many=True).dump(stack.stack_tools), 200
    return {"error": "Stack not found"}, 404


# Create a stack tool
@stack_tools_bp.route("/", methods=["POST"])
# @jwt_required()
def create_stack_tool(stack_id):
    
    stack_tool_info = Stack_ToolSchema(exclude=["stack"]).load(request.json)

    stack_tool = Stack_Tool(
        stack_id = stack_id,
        tool_id = stack_tool_info["tool"]["id"]
    )
    
    db.session.add(stack_tool)
    db.session.commit()
    
    return Stack_ToolSchema().dump(stack_tool), 201