from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.tool import Tool, ToolSchema
from blueprints.tool_steps_bp import tool_steps_bp
from setup import db
from auth import authorize


tools_bp = Blueprint("tools", __name__, url_prefix="/tools")
tools_bp.register_blueprint(tool_steps_bp)

# Get all tools
@tools_bp.route("/")
def all_tools():
    
    stmt = db.select(Tool).order_by("id")
    tools = db.session.scalars(stmt).all()
    return ToolSchema(many=True).dump(tools)


# Create a tool
@tools_bp.route("/", methods=["POST"])
@jwt_required()
def create_tool():
    
    authorize()
    
    tool_info = ToolSchema(exclude=["id"]).load(request.json)
    
    tool = Tool(
        name = tool_info["name"],
        description = tool_info.get("description", "")
    )
    
    db.session.add(tool)
    db.session.commit()
    
    return ToolSchema().dump(tool), 201


# Get a single tool
@tools_bp.route("/<int:id>")
def one_tool(id):
    
    stmt = db.select(Tool).filter_by(id = id)
    tool = db.session.scalar(stmt)
    
    if tool:
        return ToolSchema().dump(tool)
    
    return {"error": "Tool not found"}, 404


# Update a single tool
@tools_bp.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_tool(id):
    
    authorize()
    
    tool_info = ToolSchema(exclude=["id"]).load(request.json)
    
    stmt = db.select(Tool).filter_by(id = id)
    tool = db.session.scalar(stmt)
    
    if tool:
        # authorize(tool.user_id)
        tool.name = tool_info.get("name", tool.name)
        tool.description = tool_info.get("description", tool.description)
        db.session.commit()
        return ToolSchema().dump(tool), 200
    
    return {"error": "Tool not found"}, 404   


# Delete a single tool
@tools_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_tool(id):
    
    authorize()
    
    stmt = db.select(Tool).filter_by(id = id)
    tool = db.session.scalar(stmt)
    
    if tool:
        db.session.delete(tool)
        db.session.commit()
        return {"status": f"{tool.name} has been deleted"}, 200
    
    return {"error": "Tool not found"}, 404