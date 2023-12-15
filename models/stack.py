from setup import db, ma
from marshmallow import fields
from marshmallow.validate import Length


class Stack(db.Model):
    __tablename__ = "stacks"

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text)
    
    # Relationships
    stack_tools = db.relationship("Stack_Tool", back_populates="stack")
    
    
class StackSchema(ma.Schema):
    
    # Nested fields
    stack_tools = fields.Nested(
        "Stack_ToolSchema", only=["tool.name"], many=True
        )
    
    # Input Validation
    name = fields.String(
        required=True,
        validate=Length(min=1, error="name cannot be blank"),
        error_messages={"required": "The name field is required"}
        )
    description = fields.String()
    
    # Meta representation
    class Meta:
        fields = ("id", "name", "description", "stack_tools")