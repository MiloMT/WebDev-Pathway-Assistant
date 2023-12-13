from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.tool import Tool
from models.tool_step import Tool_Step, Tool_StepSchema
from setup import db
from auth import authorize


tool_steps_bp = Blueprint("tool_steps", __name__, url_prefix="/<int:tool_id>/steps")


# Get all tool steps
@tool_steps_bp.route("/")
def all_tool_steps(tool_id):
    
    stmt = db.select(Tool).filter_by(id = tool_id)
    tool = db.session.scalar(stmt)
    
    if tool:
        return Tool_StepSchema(many=True).dump(tool.tool_steps), 200
    return {"error": "Tool not found"}, 404


# Create a tool step
@tool_steps_bp.route("/", methods=["POST"])
@jwt_required()
def create_tool_step(tool_id):
    
    authorize()
    
    tool_step_info = Tool_StepSchema(exclude=["tool"]).load(request.json)
    
    tool_step = Tool_Step(
        step_no = tool_step_info["step_no"],
        description = tool_step_info.get("description", ""),
        time_days = tool_step_info["time_days"],
        tool_id = tool_id
    )
    
    db.session.add(tool_step)
    db.session.commit()
    
    return Tool_StepSchema().dump(tool_step), 201


# Get a single tool step
# @tool_steps_bp.route("/<int:id>")
# # @jwt_required()
# def one_tool_step(tool_id, id):
    
#     stmt = db.select(Tool).filter_by(id = tool_id)
#     tool = db.session.scalar(stmt)
    
#     if tool:
#         stmt = db.select(Tool_Step).filter_by(id = id)
#         return Tool_StepSchema().dump(tool.tool_steps), 200
#     return {"error": "Tool not found"}, 404


# # Update a single tool step
# @tools_bp.route("/<int:id>", methods=["PUT", "PATCH"])
# # @jwt_required()
# def update_tool(id):
    
#     tool_info = ToolSchema(exclude=["id"]).load(request.json)
    
#     stmt = db.select(Tool).filter_by(id = id)
#     tool = db.session.scalar(stmt)
    
#     if tool:
#         # authorize(tool.user_id)
#         tool.name = tool_info.get("name", tool.name)
#         tool.description = tool_info.get("description", tool.description)
#         db.session.commit()
#         return ToolSchema().dump(tool), 200
    
#     return {"error": "Tool not found"}, 404   


# # Delete a single tool step
# @tools_bp.route("/<int:id>", methods=["DELETE"])
# # @jwt_required()
# def delete_tool(id):
    
#     stmt = db.select(Tool).filter_by(id = id)
#     tool = db.session.scalar(stmt)
    
#     if tool:
#         # authorize(tool.user_id)
#         db.session.delete(tool)
#         db.session.commit()
#         return {"status": f"{tool.name} has been deleted"}, 200
    
#     return {"error": "Tool not found"}, 404