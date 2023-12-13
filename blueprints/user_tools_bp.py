from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.user import User
from models.user_tool import User_Tool, User_ToolSchema
from models.tool import Tool
from setup import db
from auth import authorize
from sqlalchemy import exc


user_tools_bp = Blueprint("user_tools", __name__, url_prefix="/<int:user_id>/tools")


# Get all user tools
@user_tools_bp.route("/")
@jwt_required()
def all_user_tools(user_id):
    
    authorize(user_id)
    
    stmt = db.select(User).filter_by(id = user_id)
    user = db.session.scalar(stmt)
    
    if user:
        return User_ToolSchema(many=True, only=["tool"]).dump(user.user_tools), 200
    
    return {"error": "User not found"}, 404


# Create a user tool
@user_tools_bp.route("/", methods=["POST"])
@jwt_required()
def create_user_tool(user_id):
    
    authorize(user_id)
    
    tool_id = (User_ToolSchema(exclude=["user"]).load(request.json))["tool"]["id"]
    
    stmt = db.select(User).filter_by(id = user_id)
    user = db.session.scalar(stmt)
    
    if user:
        stmt = db.select(Tool).filter_by(id = tool_id)
        tool = db.session.scalar(stmt)

        if tool:
            try:
                user_tool = User_Tool(
                    user_id = user_id,
                    tool_id = tool_id
                )
                db.session.add(user_tool)
                db.session.commit()
            except exc.IntegrityError:
                return {"error": "The selected tool is already added"}, 409
            
            return User_ToolSchema(exclude=["user"]).dump(user_tool), 201
        
        return {"error": "Tool not found"}, 404
    
    return {"error": "User not found"}, 404

# Delete a user tool
@user_tools_bp.route("/<int:tool_id>", methods=["DELETE"])
@jwt_required()
def delete_user_tool(user_id, tool_id):
    
    authorize(user_id)
    
    stmt = db.select(User).filter_by(id = user_id)
    user = db.session.scalar(stmt)
    
    if user:
        stmt = db.select(User_Tool).filter_by(tool_id = tool_id, user_id = user_id)
        user_tool = db.session.scalar(stmt)
        
        if user_tool:
            tool_name = (User_ToolSchema(only=["tool.name"]).dump(user_tool))["tool"]["name"]
            db.session.delete(user_tool)
            db.session.commit()
            return {"status": f"{tool_name} has been removed"}, 200
        
        return {"error": "Tool not found"}, 404
    
    return {"error": "User not found"}, 404