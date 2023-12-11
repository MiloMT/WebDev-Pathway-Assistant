from setup import db, ma
from marshmallow import fields


class Stack(db.Model):
    __tablename__ = "stacks"

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(50), default="Anonymous")
    description = db.Column(db.Text, nullable=False, unique=True)
    
    stack_tools = db.relationship("Stack_Tool", back_populates="stack")
    
    
class StackSchema(ma.Schema):
    
    stack_tools = fields.Nested(
        "Stack_ToolSchema", only=["tool.name"], many=True
        )
    
    class Meta:
        fields = ("id", "name", "description", "stack_tools")