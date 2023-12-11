from setup import db, ma
from marshmallow import fields


class Plan(db.Model):
    __tablename__ = "plans"

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(50), nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="plans")
    
class PlanSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["email", "name"])
    
    class Meta:
        fields = ("id", "name", "end_date", "user")