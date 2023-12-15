from setup import db, ma
from marshmallow import fields, EXCLUDE


class Stack_Tool(db.Model):
    __tablename__ = "stack_tools"
    
    # Columns
    stack_id = db.Column(db.Integer, db.ForeignKey("stacks.id"), nullable=False)
    tool_id = db.Column(db.Integer, db.ForeignKey("tools.id"), nullable=False)
    
    # Joined primary key
    __table_args__ = (
        db.PrimaryKeyConstraint(
            stack_id, tool_id,
        ),
    )
    
    # Relationships
    stack = db.relationship("Stack", back_populates="stack_tools")
    tool = db.relationship("Tool", back_populates="stack_tools")
    
    
class Stack_ToolSchema(ma.Schema):
    
    # Nested fields
    stack = fields.Nested("StackSchema", only=["id", "name"])
    tool = fields.Nested("ToolSchema", only=["id", "name"])
    
    # Meta representation
    class Meta:
        fields = ("stack", "tool")