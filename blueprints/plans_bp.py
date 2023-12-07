from flask import Blueprint, request
from datetime import date
# from flask_jwt_extended import jwt_required, get_jwt_identity
from models.plan import Plan, PlanSchema
from setup import db
# from auth import authorize


plans_bp = Blueprint("plans", __name__, url_prefix="/plans")


# Get all plans
@plans_bp.route("/")
# @jwt_required()
def all_plans():
    
    stmt = db.select(Plan).order_by("id")
    plans = db.session.scalars(stmt).all()
    return PlanSchema(many=True).dump(plans)


# Create a plan
@plans_bp.route("/", methods=["POST"])
# @jwt_required()
def create_plan():
    
    plan_info = PlanSchema(only=["name"]).load(request.json)
    
    plan = Plan(
        name = plan_info["name"],
        end_date = date.today() # Placeholder
    )
    
    db.session.add(plan)
    db.session.commit()
    
    return PlanSchema().dump(plan), 201


# Get a single plan
@plans_bp.route("/<int:id>")
# @jwt_required()
def one_plan(id):
    
    stmt = db.select(Plan).filter_by(id = id)
    plan = db.session.scalar(stmt)
    
    if plan:
        # authorize(plan.user_id)
        return PlanSchema().dump(plan)
    
    return {"error": "Plan not found"}, 404


# Update a single plan
@plans_bp.route("/<int:id>", methods=["PUT", "PATCH"])
# @jwt_required()
def update_plan(id):
    
    plan_info = PlanSchema(exclude=["id"]).load(request.json)
    
    stmt = db.select(Plan).filter_by(id = id)
    plan = db.session.scalar(stmt)
    
    if plan:
        # authorize(plan.user_id)
        plan.name = plan_info.get("name", plan.name)
        plan.end_date = plan_info.get("end_date", plan.end_date)
        db.session.commit()
        return PlanSchema().dump(plan), 200
    
    return {"error": "Plan not found"}, 404   


# Delete a single plan
@plans_bp.route("/<int:id>", methods=["DELETE"])
# @jwt_required()
def delete_plan(id):
    
    stmt = db.select(Plan).filter_by(id = id)
    plan = db.session.scalar(stmt)
    
    if plan:
        # authorize(plan.user_id)
        db.session.delete(plan)
        db.session.commit()
        return {"status": f"{plan.name} has been deleted"}, 200
    
    return {"error": "Plan not found"}, 404