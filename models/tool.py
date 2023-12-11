from setup import db, ma
from marshmallow import fields


class Tool(db.Model):
    __tablename__ = "tools"

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(50), default="Anonymous")
    description = db.Column(db.Text, nullable=False, unique=True)
    
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    category = db.relationship("Category", back_populates="tools")
    
    language_id = db.Column(db.Integer, db.ForeignKey("languages.id"), nullable=False)
    language = db.relationship("Language", back_populates="tools")
    
class ToolSchema(ma.Schema):
    
    category = fields.Nested("CategorySchema", only=["name"])
    language = fields.Nested("LanguageSchema", only=["name"])
    
    class Meta:
        fields = ("id", "name", "description", "category", "language")