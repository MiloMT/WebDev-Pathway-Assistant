from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required
from models.stack import Stack
from models.stack_tool import Stack_Tool, Stack_ToolSchema
from models.tool import Tool
from setup import db
from auth import authorize
from sqlalchemy import exc


stack_tools_bp = Blueprint("stack_tools", __name__, url_prefix="/<int:stack_id>/tools")

# Get all stack tools
@stack_tools_bp.route("/")
def all_stack_tools(stack_id):
    
    # Query to obtain a JSON of the specific stack.
    # Due to established relations, the tool details can be read
    # from the stack
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
    
    # Query to obtain a JSON of the specific stack
    # with the ID taken from the route
    stmt = db.select(Stack).filter_by(id = stack_id)
    stack = db.session.scalar(stmt)
    
    if stack:
        tool_id = (Stack_ToolSchema(exclude=["stack"]).load(request.json, partial=True))["tool"]["id"]

        # Query to obtain a JSON of the specific tool
        # with the ID taken from the JSON request
        stmt = db.select(Tool).filter_by(id = tool_id)
        tool = db.session.scalar(stmt)

        if tool:
            stack_tool = Stack_Tool(
                stack_id = stack_id,
                tool_id = tool_id
            )
            try:
                db.session.add(stack_tool)
                db.session.commit()
            except exc.IntegrityError:
                return {"error": "The selected tool is already added"}, 409
            
            return Stack_ToolSchema(exclude=["stack"]).dump(stack_tool), 201
    
        return {"error": "Tool not found"}, 404
    
    return {"error": "Stack not found"}, 404
    

# Delete a stack tool
@stack_tools_bp.route("/<int:tool_id>", methods=["DELETE"])
@jwt_required()
def delete_stack_tool(stack_id, tool_id):
    
    authorize()
    
    # Query to obtain a JSON of the specific stack
    # with the ID taken from the route
    stmt = db.select(Stack).filter_by(id = stack_id)
    stack = db.session.scalar(stmt)
    
    if stack:
        # Query to obtain a JSON of the specific stack_tool
        # where the IDs of both the stack and tool match the ID's
        # provided by the route.
        stmt = db.select(Stack_Tool).filter_by(tool_id = tool_id, stack_id = stack_id)
        stack_tool = db.session.scalar(stmt)
        
        if stack_tool:
            tool_name = (Stack_ToolSchema(only=["tool.name"]).dump(stack_tool))["tool"]["name"]
            db.session.delete(stack_tool)
            db.session.commit()
            return {"status": f"{tool_name} has been removed"}, 200
        
        return {"error": "Tool not found"}, 404
    
    return {"error": "Stack not found"}, 404