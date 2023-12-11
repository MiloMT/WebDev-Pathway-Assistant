from setup import db, ma
from marshmallow import fields


class User_Tool(db.Model):
    __tablename__ = "user_tools"
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="user_tools")
    
    tool_id = db.Column(db.Integer, db.ForeignKey("tools.id"), nullable=False)
    tool = db.relationship("Tool", back_populates="user_tools")
    
    __table_args__ = (
        db.PrimaryKeyConstraint(
            user_id, tool_id,
        ),
    )
    
class User_ToolSchema(ma.Schema):
    
    user = fields.Nested("UserSchema", only=["email", "name"])
    tool = fields.Nested("ToolSchema", only=["id", "name"])
    
    class Meta:
        fields = ("user", "tool")