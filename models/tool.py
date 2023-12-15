from setup import db, ma
from marshmallow import fields
from marshmallow.validate import Length


class Tool(db.Model):
    __tablename__ = "tools"

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text)
    category_id = db.Column(
        db.Integer, 
        db.ForeignKey("categories.id"), 
        nullable=False
        )
    language_id = db.Column(
        db.Integer, 
        db.ForeignKey("languages.id"), 
        nullable=False
        )
    
    # Relationships
    category = db.relationship("Category", back_populates="tools")
    language = db.relationship("Language", back_populates="tools")
    tool_steps = db.relationship("Tool_Step", back_populates="tool")
    stack_tools = db.relationship("Stack_Tool", back_populates="tool")
    user_tools = db.relationship("User_Tool", back_populates="tool")
    
class ToolSchema(ma.Schema):
    
    # Nested fields
    category = fields.Nested("CategorySchema", only=["id", "name"])
    language = fields.Nested("LanguageSchema", only=["id", "name"])
    tool_steps = fields.Nested(
        "Tool_StepSchema", 
        only=["step_no", "description", "time_days"], 
        many=True
        )
    
    # Input Validation
    name = fields.String(
        required=True,
        validate=Length(min=1, error="name cannot be blank")
        )
    description = fields.String()
    
    # Meta Representation
    class Meta:
        fields = (
            "id", 
            "name", 
            "description", 
            "category", 
            "language", 
            "tool_steps"
            )