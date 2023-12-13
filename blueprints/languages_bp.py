from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.language import Language, LanguageSchema
from setup import db
from auth import authorize


languages_bp = Blueprint("languages", __name__, url_prefix="/languages")


# Get all languages
@languages_bp.route("/")
def all_languages():
    
    stmt = db.select(Language).order_by("id")
    languages = db.session.scalars(stmt).all()
    return LanguageSchema(many=True).dump(languages)


# Create a language
@languages_bp.route("/", methods=["POST"])
@jwt_required()
def create_language():
    
    authorize()
    
    language_info = LanguageSchema(exclude=["id"]).load(request.json)
    language = Language(name = language_info["name"])
    
    db.session.add(language)
    db.session.commit()
    
    return LanguageSchema().dump(language), 201


# Get a single language
@languages_bp.route("/<int:id>")
def one_language(id):
    
    stmt = db.select(Language).filter_by(id = id)
    language = db.session.scalar(stmt)
    
    if language:
        return LanguageSchema().dump(language)
    
    return {"error": "Language not found"}, 404


# Update a single language
@languages_bp.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_language(id):
    
    authorize()
    
    language_info = LanguageSchema(exclude=["id"]).load(request.json)
    
    stmt = db.select(Language).filter_by(id = id)
    language = db.session.scalar(stmt)
    
    if language:
        language.name = language_info.get("name", language.name)
        db.session.commit()
        return LanguageSchema().dump(language), 200
    
    return {"error": "Language not found"}, 404   


# Delete a single language
@languages_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_language(id):
    
    authorize()
    
    stmt = db.select(Language).filter_by(id = id)
    language = db.session.scalar(stmt)
    
    if language:
        db.session.delete(language)
        db.session.commit()
        return {"status": f"{language.name} has been deleted"}, 200
    
    return {"error": "Language not found"}, 404