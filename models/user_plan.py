# Need to develop further, commenting out for now.

# from setup import db, ma
# from marshmallow import fields


# class User_Plan(db.Model):
#     __tablename__ = "plans"

#     id = db.Column(db.Integer)
    
#     name = db.Column(db.String(50), nullable=False)
#     end_date = db.Column(db.Date, nullable=False)
    
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
#     user = db.relationship("User", back_populates="plans")
    
#     __table_args__ = (
#         db.PrimaryKeyConstraint(
#             user_id, id,
#         ),
#     )
    
# class User_PlanSchema(ma.Schema):
#     user = fields.Nested("UserSchema", only=["email", "name"])
    
#     class Meta:
#         fields = ("id", "name", "end_date", "user")