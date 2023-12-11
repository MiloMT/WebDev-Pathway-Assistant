from setup import db, ma
from marshmallow import fields
from marshmallow.validate import Length


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.Text, default="Anonymous")
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    plans = db.relationship("Plan", back_populates="user")
    user_tools = db.relationship("User_Tool", back_populates="user")
    
    
class UserSchema(ma.Schema):
    
    plans = fields.Nested("PlanSchema", many=True, only=["id", "name", "end_date"])
    user_tools = fields.Nested(
        "User_ToolSchema", only=["tool"], many=True
        )
    
    email = fields.Email(required=True)
    password = fields.String(
        required=True, 
        validate=Length(
            min=8, error="Password must be at least 8 characters"
            )
        )
    
    class Meta:
        fields = ("id", "name", "email", "password", "is_admin", "plans", "user_tools")