from setup import db, ma
from marshmallow import fields
from marshmallow.validate import Length


class Tool_Step(db.Model):
    __tablename__ = "tool_steps"
    
    # Columns
    step_no = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    time_days = db.Column(db.Integer, nullable=False)
    tool_id = db.Column(db.Integer, db.ForeignKey("tools.id"), nullable=False)
    
    # Joined primary key
    __table_args__ = (
        db.PrimaryKeyConstraint(
            tool_id, step_no,
        ),
    )
    
    # Relationships
    tool = db.relationship("Tool", back_populates="tool_steps")
    
    
class Tool_StepSchema(ma.Schema):
    
    # Nested fields
    tool = fields.Nested("ToolSchema", only=["name"])
    
    # Input Validation
    step_no = fields.Integer(required=True)
    description = fields.String(
        required=True,
        validate=Length(min=1, error="name cannot be blank")
        )
    time_days = fields.Integer(required=True)
    
    # Meta representation
    class Meta:
        fields = ("step_no", "description", "time_days", "tool")