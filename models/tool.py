from setup import db, ma
from marshmallow import fields


class Tool(db.Model):
    __tablename__ = "tools"

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.Text, nullable=False)
    
    category_id = db.Column(
        db.Integer, db.ForeignKey("categories.id"), nullable=False
        )
    category = db.relationship("Category", back_populates="tools")
    
    language_id = db.Column(
        db.Integer, db.ForeignKey("languages.id"), nullable=False
        )
    language = db.relationship("Language", back_populates="tools")
    
    tool_steps = db.relationship("Tool_Step", back_populates="tool")
    stack_tools = db.relationship("Stack_Tool", back_populates="tool")
    user_tools = db.relationship("User_Tool", back_populates="tool")
    
class ToolSchema(ma.Schema):
    
    category = fields.Nested(
        "CategorySchema", only=["name"]
        )
    language = fields.Nested(
        "LanguageSchema", only=["name"]
        )
    tool_steps = fields.Nested(
        "Tool_StepSchema", 
        only=["step_no", "description", "time_days"], 
        many=True
        )
    
    class Meta:
        fields = (
            "id", 
            "name", 
            "description", 
            "category", 
            "language", 
            "tool_steps"
            )