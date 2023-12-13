# Need to develop further, commenting out for now.

# from flask import Blueprint, request
# from datetime import date
# from flask_jwt_extended import jwt_required
# from models.user_plan import User_Plan, User_PlanSchema
# from setup import db
# from auth import authorize


# user_plans_bp = Blueprint("plans", __name__, url_prefix="/<int:user_id>/plans")


# # Get all plans
# @user_plans_bp.route("/")
# @jwt_required()
# def all_plans(user_id):
    
#     authorize(user_id)
    
#     stmt = db.select(User_Plan).order_by("id")
#     plans = db.session.scalars(stmt).all()
#     return User_PlanSchema(many=True).dump(plans)


# # Create a plan
# @user_plans_bp.route("/", methods=["POST"])
# @jwt_required()
# def create_plan(user_id):
    
#     authorize(user_id)
    
#     user_plan_info = User_PlanSchema(only=["name"]).load(request.json)
    
#     user_plan = User_Plan(
#         name = user_plan_info["name"],
#         end_date = date.today() # Placeholder
#     )
    
#     db.session.add(user_plan)
#     db.session.commit()
    
#     return User_PlanSchema().dump(user_plan), 201


# # Get a single plan
# @user_plans_bp.route("/<int:plan_id>")
# @jwt_required()
# def one_plan(user_id, plan_id):
    
#     stmt = db.select(User_Plan).filter_by(plan_id = id)
#     user_plan = db.session.scalar(stmt)
    
#     if user_plan:
#         authorize(user_id)
#         return User_PlanSchema().dump(user_plan)
    
#     return {"error": "Plan not found"}, 404


# # Update a single plan
# @user_plans_bp.route("/<int:plan_id>", methods=["PUT", "PATCH"])
# @jwt_required()
# def update_plan(user_id, plan_id):
    
#     user_plan_info = User_PlanSchema(exclude=["id"]).load(request.json)
    
#     stmt = db.select(User_Plan).filter_by(plan_id = id)
#     user_plan = db.session.scalar(stmt)
    
#     if user_plan:
#         authorize(user_id)
#         user_plan.name = user_plan_info.get("name", user_plan.name)
#         user_plan.end_date = user_plan_info.get("end_date", user_plan.end_date)
#         db.session.commit()
#         return User_PlanSchema().dump(user_plan), 200
    
#     return {"error": "Plan not found"}, 404   


# # Delete a single plan
# @user_plans_bp.route("/<int:plan_id>", methods=["DELETE"])
# @jwt_required()
# def delete_plan(user_id, plan_id):
    
#     stmt = db.select(User_Plan).filter_by(plan_id = id)
#     user_plan = db.session.scalar(stmt)
    
#     if user_plan:
#         authorize(user_id)
#         db.session.delete(user_plan)
#         db.session.commit()
#         return {"status": f"{user_plan.name} has been deleted"}, 200
    
#     return {"error": "Plan not found"}, 404