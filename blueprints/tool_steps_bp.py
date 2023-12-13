from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.tool import Tool
from models.tool_step import Tool_Step, Tool_StepSchema
from setup import db
from auth import authorize
from operator import itemgetter
from sqlalchemy import exc


tool_steps_bp = Blueprint("tool_steps", __name__, url_prefix="/<int:tool_id>/steps")


# Get all tool steps
@tool_steps_bp.route("/")
def all_tool_steps(tool_id):
    
    stmt = db.select(Tool).filter_by(id = tool_id)
    tool = db.session.scalar(stmt)
    
    if tool:
        return sorted(
            Tool_StepSchema(many=True, exclude=["tool"]).dump(tool.tool_steps), key=itemgetter("step_no")
            ), 200
        
    return {"error": "Tool not found"}, 404


# Create a tool step
@tool_steps_bp.route("/", methods=["POST"])
@jwt_required()
def create_tool_step(tool_id):
    
    authorize()
    
    stmt = db.select(Tool).filter_by(id = tool_id)
    tool = db.session.scalar(stmt)
    
    if tool:
        tool_step_info = Tool_StepSchema(exclude=["tool"]).load(request.json)
        tool_step = Tool_Step(
            step_no = tool_step_info["step_no"],
            description = tool_step_info.get("description", ""),
            time_days = tool_step_info["time_days"],
            tool_id = tool_id
        )
        try:
            db.session.add(tool_step)
            db.session.commit()
        except exc.IntegrityError:
            return {"error": "The selected step number already exists"}, 409
        
        return Tool_StepSchema(exclude=["tool"]).dump(tool_step), 201
    
    return {"error": "Tool not found"}, 404


# Get a single tool step
@tool_steps_bp.route("/<int:step_no>")
def get_tool_step(tool_id, step_no):
    
    stmt = db.select(Tool).filter_by(id = tool_id)
    tool = db.session.scalar(stmt)
    
    if tool:
        stmt = db.select(Tool_Step).filter_by(tool_id = tool_id, step_no = step_no)
        tool_step = db.session.scalar(stmt)
        
        if tool_step:
            return Tool_StepSchema(exclude=["tool"]).dump(tool_step), 200
        
        return {"error": "Step not found"}, 404
    
    return {"error": "Tool not found"}, 404


# Update a single tool step
@tool_steps_bp.route("/<int:step_no>", methods=["PUT", "PATCH"])
@jwt_required()
def update_tool_step(tool_id, step_no):
    
    authorize()
    
    tool_step_info = Tool_StepSchema(exclude=["tool"]).load(request.json)
    
    stmt = db.select(Tool).filter_by(id = tool_id)
    tool = db.session.scalar(stmt)
    
    if tool:
        stmt = db.select(Tool_Step).filter_by(tool_id = tool_id, step_no = step_no)
        tool_step = db.session.scalar(stmt)
        
        if tool_step:
            tool_step.step_no = tool_step_info.get("step_no", tool_step.step_no)
            tool_step.description = tool_step_info.get("description", tool_step.description)
            tool_step.time_days = tool_step_info.get("time_days", tool_step.time_days)
            
            try:
                db.session.commit()
            except exc.IntegrityError:
                return {"error": "The selected step number already exists"}, 409
            
            return Tool_StepSchema(exclude=["tool"]).dump(tool_step), 200
        
        return {"error": "Step not found"}, 404
    
    return {"error": "Tool not found"}, 404   


# Delete a single tool step
@tool_steps_bp.route("/<int:step_no>", methods=["DELETE"])
@jwt_required()
def delete_tool_step(tool_id, step_no):
    
    authorize()
    
    stmt = db.select(Tool).filter_by(id = tool_id)
    tool = db.session.scalar(stmt)
    
    if tool:
        stmt = db.select(Tool_Step).filter_by(tool_id = tool_id, step_no = step_no)
        tool_step = db.session.scalar(stmt)
        
        if tool_step:
            db.session.delete(tool_step)
            db.session.commit()
            return {"status": f"Tool Step {tool_step.step_no} has been deleted"}, 200
    
        return {"error": "Step not found"}, 404
    
    return {"error": "Tool not found"}, 404