from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from os import environ
from sqlalchemy.exc import DataError
from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import BadRequest, UnsupportedMediaType

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")
app.config["JWT_SECRET_KEY"] = environ.get("JWT_KEY")

db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

@app.errorhandler(401)
def unauthorized(err):
    return {"error": "You are not authorized to access this URL"}, 401

@app.errorhandler(ValidationError)
def validation_error(err):
    return {"error": err.messages}, 400

@app.errorhandler(KeyError)
def key_error(err):
    return {"error": f"The field {err} is required"}, 400

@app.errorhandler(BadRequest)
def bad_request(err):
    return {"error": err.description}, 400

@app.errorhandler(UnsupportedMediaType)
def unsupported_media_type(err):
    return {"error": err.description}, 415

@app.errorhandler(DataError)
def data_error(err):
    return {"error": str(err.orig).split(":")[0]}, 400