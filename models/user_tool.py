from setup import db, ma
from marshmallow import fields
from marshmallow.validate import Length


class User_Tool(db.Model):
    __tablename__ = "user_tools"
    
    # Columns
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    tool_id = db.Column(db.Integer, db.ForeignKey("tools.id"), nullable=False)
    
    # Joined primary key
    __table_args__ = (
        db.PrimaryKeyConstraint(
            user_id, tool_id,
        ),
    )
    
    # Relationships
    user = db.relationship("User", back_populates="user_tools")
    tool = db.relationship("Tool", back_populates="user_tools")
    
    
class User_ToolSchema(ma.Schema):
    
    # Nested fields
    user = fields.Nested("UserSchema", only=["email", "name"])
    tool = fields.Nested("ToolSchema", only=["id", "name"])
    
    # Meta representation
    class Meta:
        fields = ("user", "tool")