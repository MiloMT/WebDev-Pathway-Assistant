from setup import db, ma


class Plan(db.Model):
    __tablename__ = "plans"

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(50), nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    
    
class PlanSchema(ma.Schema):
    
    class Meta:
        fields = ("id", "name", "end_date")