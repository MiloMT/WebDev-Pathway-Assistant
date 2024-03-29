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
    
    # Query to obtain a JSON of tools ordered by their ID
    stmt = db.select(Tool).order_by("id")
    tools = db.session.scalars(stmt).all()
    
    return ToolSchema(many=True, exclude=["tool_steps", "category.id", "language.id"]).dump(tools)


# Create a tool
@tools_bp.route("/", methods=["POST"])
@jwt_required()
def create_tool():
    
    authorize()
    
    tool_info = ToolSchema(exclude=["id"]).load(request.json, partial=True)
    
    tool = Tool(
        name = tool_info["name"],
        description = tool_info.get("description", ""),
        category_id = tool_info.get("category", {}).get("id"),
        language_id = tool_info.get("language", {}).get("id")
    )
        
    try:
        db.session.add(tool)
        db.session.commit()
    except exc.IntegrityError as e:
        if all(x in str(e.orig) for x in ["category_id", "Failing row"]):
            return {"error": "Ensure that the category ID is included in the request"}, 409
        elif "category_id" in str(e.orig):
            return {"error": "Category specified can't be found"}, 409
        elif all(x in str(e.orig) for x in ["language_id", "Failing row"]):
            return {"error": "Ensure that the language ID is included in the request"}, 409
        elif "language_id" in str(e.orig):
            return {"error": "Language specified can't be found"}, 409
        else:
            return {"error": "The tool name already exists"}, 409
    
    return ToolSchema(exclude=["tool_steps", "category.id", "language.id"]).dump(tool), 201


# Get a single tool
@tools_bp.route("/<int:tool_id>")
def get_tool(tool_id):
    
    # Query to obtain a JSON of the specific tool
    # with the ID taken from the route
    stmt = db.select(Tool).filter_by(id = tool_id)
    tool = db.session.scalar(stmt)
    
    if tool:
        return ToolSchema(exclude=["tool_steps", "category.id", "language.id"]).dump(tool)
    
    return {"error": "Tool not found"}, 404


# Update a single tool
@tools_bp.route("/<int:tool_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_tool(tool_id):
    
    authorize()
    
    tool_info = ToolSchema(exclude=["id"]).load(request.json, partial=True)
    
    # Query to obtain a JSON of the specific tool
    # with the ID taken from the route
    stmt = db.select(Tool).filter_by(id = tool_id)
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
@tools_bp.route("/<int:tool_id>", methods=["DELETE"])
@jwt_required()
def delete_tool(tool_id):
    
    authorize()
    
    # Query to obtain a JSON of the specific tool
    # with the ID taken from the route
    stmt = db.select(Tool).filter_by(id = tool_id)
    tool = db.session.scalar(stmt)
    
    if tool:
        try:
            db.session.delete(tool)
            db.session.commit()
        except (exc.IntegrityError, AssertionError):
            return {"error": "This tool is linked to other resources. Dependencies must be removed first."}, 409
        
        return {"status": f"{tool.name} has been deleted"}, 200
    
    return {"error": "Tool not found"}, 404