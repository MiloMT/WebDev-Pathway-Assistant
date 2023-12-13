from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required
from models.stack import Stack
from models.stack_tool import Stack_Tool, Stack_ToolSchema
from models.tool import Tool
from setup import db
from auth import authorize


stack_tools_bp = Blueprint("stack_tools", __name__, url_prefix="/<int:stack_id>/tools")

# Get all stack tools
@stack_tools_bp.route("/")
def all_stack_tools(stack_id):
    
    stmt = db.select(Stack).filter_by(id = stack_id)
    stack = db.session.scalar(stmt)
    
    if stack:
        return Stack_ToolSchema(many=True, only=["tool"]).dump(stack.stack_tools), 200
    
    return {"error": "Stack not found"}, 404
    


# Create a stack tool
@stack_tools_bp.route("/", methods=["POST"])
@jwt_required()
def create_stack_tool(stack_id):
    
    authorize()
    
    stmt = db.select(Stack).filter_by(id = stack_id)
    stack = db.session.scalar(stmt)
    
    if stack:
        tool_id = (Stack_ToolSchema(exclude=["stack"]).load(request.json))["tool"]["id"]

        stmt = db.select(Tool).filter_by(id = tool_id)
        tool = db.session.scalar(stmt)

        if tool:
            stack_tool = Stack_Tool(
                stack_id = stack_id,
                tool_id = tool_id
            )
        
            db.session.add(stack_tool)
            db.session.commit()
            
            return Stack_ToolSchema(exclude=["stack"]).dump(stack_tool), 201
    
        return {"error": "Tool not found"}, 404
    
    return {"error": "Stack not found"}, 404
    

# Delete a stack tool
@stack_tools_bp.route("/<int:tool_id>", methods=["DELETE"])
@jwt_required()
def delete_stack_tool(stack_id, tool_id):
    
    authorize()
    
    stmt = db.select(Stack).filter_by(id = stack_id)
    stack = db.session.scalar(stmt)
    
    if stack:
        stmt = db.select(Stack_Tool).filter_by(tool_id = tool_id, stack_id = stack_id)
        stack_tool = db.session.scalar(stmt)
        
        if stack_tool:
            tool_name = (Stack_ToolSchema(only=["tool.name"]).dump(stack_tool))["tool"]["name"]
            db.session.delete(stack_tool)
            db.session.commit()
            return {"status": f"{tool_name} has been removed"}, 200
        
        return {"error": "Tool not found"}, 404
    
    return {"error": "Stack not found"}, 404