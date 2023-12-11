from setup import db, ma


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    tools = db.relationship("Tool", back_populates="category")
    
    
class CategorySchema(ma.Schema):
    
    class Meta:
        fields = ("id", "name", "description")