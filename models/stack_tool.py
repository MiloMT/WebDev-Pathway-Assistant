from setup import db, ma
from marshmallow import fields


class Stack_Tool(db.Model):
    __tablename__ = "stack_tools"
    
    stack_id = db.Column(db.Integer, db.ForeignKey("stacks.id"), nullable=False)
    stack = db.relationship("Stack", back_populates="stack_tools")
    
    tool_id = db.Column(db.Integer, db.ForeignKey("tools.id"), nullable=False)
    tool = db.relationship("Tool", back_populates="stack_tools")
    
    __table_args__ = (
        db.PrimaryKeyConstraint(
            stack_id, tool_id,
        ),
    )
    
class Stack_ToolSchema(ma.Schema):
    
    stack = fields.Nested("StackSchema", only=["id", "name"])
    tool = fields.Nested("ToolSchema", only=["id", "name"])
    
    class Meta:
        fields = ("stack", "tool")