from setup import db, ma
from marshmallow import fields


class Tool_Step(db.Model):
    __tablename__ = "tool_steps"
    
    step_no = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    time_days = db.Column(db.Integer, nullable=False)
    
    tool_id = db.Column(db.Integer, db.ForeignKey("tools.id"), nullable=False)
    tool = db.relationship("Tool", back_populates="tool_steps")
    
    __table_args__ = (
        db.PrimaryKeyConstraint(
            tool_id, step_no,
        ),
    )
    
class Tool_StepSchema(ma.Schema):
    
    tool = fields.Nested("ToolSchema", only=["name"])
    
    class Meta:
        fields = ("step_no", "description", "time_days", "tool")