from src.db import db
from ...utils import NameSpace

FoodNamesSpace = NameSpace.Schemas.FoodSchema

class FoodPortionTypeModel(db.Model):
    __tablename__ = FoodNamesSpace.FoodProtionType.TABLE_NAME
    __table_args__ = { "schema":FoodNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), nullable=False,unique=True)
    description = db.Column(db.String(256), nullable=False)
    foods = db.relationship("FoodModel", back_populates="food_portion_types", secondary=f"{FoodNamesSpace.SCHEMA_NAME}.{FoodNamesSpace.MapFoodFoodPortionType.TABLE_NAME}")


    def __init__(self, data):
        id = data.get(FoodNamesSpace.FoodProtionType.ID)
        self.type = data.get(FoodNamesSpace.FoodProtionType.TYPE)
        self.description = data.get(FoodNamesSpace.FoodProtionType.DESCRIPTION)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()





