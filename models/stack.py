from setup import db, ma


class Stack(db.Model):
    __tablename__ = "stacks"

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(50), default="Anonymous")
    description = db.Column(db.Text, nullable=False, unique=True)
    
    
class StackSchema(ma.Schema):
    
    class Meta:
        fields = ("id", "name", "description")