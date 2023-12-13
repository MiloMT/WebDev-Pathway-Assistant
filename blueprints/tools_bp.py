from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.tool import Tool, ToolSchema
from blueprints.tool_steps_bp import tool_steps_bp
from setup import db
from auth import authorize
from sqlalchemy import exc


tools_bp = Blueprint("tools", __name__, url_prefix="/tools")
tools_bp.register_blueprint(tool_steps_bp)

# Get all tools
@tools_bp.route("/")
def all_tools():
    
    stmt = db.select(Tool).order_by("id")
    tools = db.session.scalars(stmt).all()
    
    return ToolSchema(many=True, exclude=["tool_steps", "category.id", "language.id"]).dump(tools)


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
    
    try:
        db.session.add(tool)
        db.session.commit()
    except exc.IntegrityError:
            return {"error": "The tool name already exists"}, 409
    
    return ToolSchema().dump(tool), 201


# Get a single tool
@tools_bp.route("/<int:id>")
def get_tool(id):
    
    stmt = db.select(Tool).filter_by(id = id)
    tool = db.session.scalar(stmt)
    
    if tool:
        return ToolSchema(exclude=["tool_steps"]).dump(tool)
    
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
        tool.name = tool_info.get("name", tool.name)
        tool.description = tool_info.get("description", tool.description)
        
        try:
            if "category" in tool_info:
                tool.category_id = tool_info.get("category").get("id", tool.category.id)
            if "language" in tool_info:
                tool.language_id = tool_info.get("language").get("id", tool.language.id)
        
            db.session.commit()
            
            return ToolSchema(exclude=["tool_steps", "category.id", "language.id"]).dump(tool), 200
        except exc.IntegrityError as e:
            if "category_id" in str(e.orig):
                return {"error": "Category specified can't be found"}, 409
            elif "language_id" in str(e.orig):
                return {"error": "Language specified can't be found"}, 409
            else:
                return {"error": "The tool name already exists"}, 409
    
    return {"error": "Tool not found"}, 404   


# Delete a single tool
@tools_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_tool(id):
    
    authorize()
    
    stmt = db.select(Tool).filter_by(id = id)
    tool = db.session.scalar(stmt)
    
    if tool:
        try:
            db.session.delete(tool)
            db.session.commit()
        except exc.IntegrityError:
            return {"error": "This tool is linked to other resources. Dependencies must be removed first."}, 409
        
        return {"status": f"{tool.name} has been deleted"}, 200
    
    return {"error": "Tool not found"}, 404