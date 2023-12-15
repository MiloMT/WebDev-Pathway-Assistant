from setup import db, ma
from marshmallow import fields
from marshmallow.validate import Length


class User(db.Model):
    __tablename__ = "users"

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    # Relationships
    user_tools = db.relationship("User_Tool", back_populates="user")
    
    
class UserSchema(ma.Schema):
    
    # Nested fields
    user_tools = fields.Nested("User_ToolSchema", many=True, only=["tool.name"])
    
    # Input validation
    email = fields.Email(required=True)
    password = fields.String(
        required=True,
        validate=Length(min=8, error="Password must be at least 8 characters")
        )
    name = fields.String(required=True)
    is_admin = fields.Boolean()
    
    # Meta representation
    class Meta:
        fields = ("id", "name", "email", "password", "is_admin", "user_tools")