from setup import db, ma


class Language(db.Model):
    __tablename__ = "languages"

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(50), nullable=False, unique=True)
    
    
class LanguageSchema(ma.Schema):
    
    class Meta:
        fields = ("id", "name")