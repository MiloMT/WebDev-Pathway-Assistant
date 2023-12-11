from flask import Blueprint, request
# from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User, UserSchema
from models.user_tool import User_Tool, User_ToolSchema
from setup import db
# from auth import authorize


user_tools_bp = Blueprint("user_tools", __name__, url_prefix="/<int:user_id>/tools")


# Get all user tools
@user_tools_bp.route("/")
# @jwt_required()
def all_user_tools(user_id):
    
    stmt = db.select(User).filter_by(id = user_id)
    user = db.session.scalar(stmt)
    
    if user:
        return User_ToolSchema(many=True).dump(user.user_tools), 200
    return {"error": "User not found"}, 404


# Create a user tool
@user_tools_bp.route("/", methods=["POST"])
# @jwt_required()
def create_user_tool(user_id):
    
    print("Running creation route")
    
    user_tool_info = User_ToolSchema(exclude=["user_id"]).load(request.json)
    
    print("Finished load")
    print(user_tool_info)

    user_tool = User_Tool(
        user_id = user_id,
        tool_id = user_tool_info["tool_id"]
    )
    
    db.session.add(user_tool)
    db.session.commit()
    
    return User_ToolSchema().dump(user_tool), 201