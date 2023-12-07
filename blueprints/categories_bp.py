from flask import Blueprint, request
# from flask_jwt_extended import jwt_required, get_jwt_identity
from models.category import Category, CategorySchema
from setup import db
# from auth import authorize


categories_bp = Blueprint("categories", __name__, url_prefix="/categories")


# Get all categories
@categories_bp.route("/")
# @jwt_required()
def all_categories():
    
    stmt = db.select(Category).order_by("id")
    categories = db.session.scalars(stmt).all()
    return CategorySchema(many=True).dump(categories)


# Create a category
@categories_bp.route("/", methods=["POST"])
# @jwt_required()
def create_category():
    
    category_info = CategorySchema(exclude=["id"]).load(request.json)
    
    category = Category(
        name = category_info["name"],
        description = category_info.get("description", "")
    )
    
    db.session.add(category)
    db.session.commit()
    
    return CategorySchema().dump(category), 201


# Get a single category
@categories_bp.route("/<int:id>")
# @jwt_required()
def one_category(id):
    
    stmt = db.select(Category).filter_by(id = id)
    category = db.session.scalar(stmt)
    
    if category:
        # authorize(category.user_id)
        return CategorySchema().dump(category)
    
    return {"error": "Category not found"}, 404


# Update a single category
@categories_bp.route("/<int:id>", methods=["PUT", "PATCH"])
# @jwt_required()
def update_category(id):
    
    category_info = CategorySchema(exclude=["id"]).load(request.json)
    
    stmt = db.select(Category).filter_by(id = id)
    category = db.session.scalar(stmt)
    
    if category:
        # authorize(category.user_id)
        category.name = category_info.get("name", category.name)
        category.description = category_info.get("description", category.description)
        db.session.commit()
        return CategorySchema().dump(category), 200
    
    return {"error": "Category not found"}, 404   


# Delete a single category
@categories_bp.route("/<int:id>", methods=["DELETE"])
# @jwt_required()
def delete_category(id):
    
    stmt = db.select(Category).filter_by(id = id)
    category = db.session.scalar(stmt)
    
    if category:
        # authorize(category.user_id)
        db.session.delete(category)
        db.session.commit()
        return {"status": f"{category.name} has been deleted"}, 200
    
    return {"error": "Category not found"}, 404