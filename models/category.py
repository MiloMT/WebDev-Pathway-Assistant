from setup import db, ma
from marshmallow import fields
from marshmallow.validate import Length


class Category(db.Model):
    __tablename__ = "categories"

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # Relationships
    tools = db.relationship("Tool", back_populates="category")
    
    
class CategorySchema(ma.Schema):
    
    # Input Validation
    name = fields.String(
        required=True,
        validate=Length(min=1, error="name cannot be blank"),
        error_messages={"required": "The name field is required"}
        )
    
    # Meta representation
    class Meta:
        fields = ("id", "name", "description")