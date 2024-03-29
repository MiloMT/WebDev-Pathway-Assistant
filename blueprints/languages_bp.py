from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.language import Language, LanguageSchema
from setup import db
from auth import authorize
from sqlalchemy import exc


languages_bp = Blueprint("languages", __name__, url_prefix="/languages")


# Get all languages
@languages_bp.route("/")
def all_languages():
    
    # Query to obtain a JSON of languages ordered by their ID
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
    
    try:
        db.session.add(language)
        db.session.commit()
    except exc.IntegrityError:
        return {"error": "The language name already exists"}, 409
    
    return LanguageSchema().dump(language), 201


# Get a single language
@languages_bp.route("/<int:language_id>")
def get_language(language_id):
    
    # Query to obtain a JSON of the specific language
    # with the ID taken from the route
    stmt = db.select(Language).filter_by(id = language_id)
    language = db.session.scalar(stmt)
    
    if language:
        return LanguageSchema().dump(language)
    
    return {"error": "Language not found"}, 404


# Update a single language
@languages_bp.route("/<int:language_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_language(language_id):
    
    authorize()
    
    language_info = LanguageSchema(exclude=["id"]).load(request.json)
    
    # Query to obtain a JSON of the specific language
    # with the ID taken from the route
    stmt = db.select(Language).filter_by(id = language_id)
    language = db.session.scalar(stmt)
    
    if language:
        language.name = language_info.get("name", language.name)
        
        try:
            db.session.commit()
        except exc.IntegrityError:
            return {"error": "The language name already exists"}, 409
        
        return LanguageSchema().dump(language), 200
    
    return {"error": "Language not found"}, 404   


# Delete a single language
@languages_bp.route("/<int:language_id>", methods=["DELETE"])
@jwt_required()
def delete_language(language_id):
    
    authorize()
    
    # Query to obtain a JSON of the specific language
    # with the ID taken from the route
    stmt = db.select(Language).filter_by(id = language_id)
    language = db.session.scalar(stmt)
    
    if language:
        try:
            db.session.delete(language)
            db.session.commit()
        except exc.IntegrityError:
            return {"error": "This language is linked to other resources. Dependencies must be removed first."}, 409
        
        return {"status": f"{language.name} has been deleted"}, 200
    
    return {"error": "Language not found"}, 404