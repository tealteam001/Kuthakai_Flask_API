from src.db import db
from ...utils import NameSpace

FoodNamesSpace = NameSpace.Schemas.FoodSchema


class MapFoodFoodPortionType(db.Model):
    __tablename__ = FoodNamesSpace.MapFoodFoodPortionType.TABLE_NAME
    __table_args__ = { "schema":FoodNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey(f"{FoodNamesSpace.SCHEMA_NAME}.{FoodNamesSpace.Food.TABLE_NAME}.{FoodNamesSpace.Food.ID}"),nullable=False)
    food_portion_type_id = db.Column(db.Integer,db.ForeignKey(f"{FoodNamesSpace.SCHEMA_NAME}.{FoodNamesSpace.FoodProtionType.TABLE_NAME}.{FoodNamesSpace.FoodProtionType.ID}"),nullable=False)

    def __init__(self, data):
        id = data.get(FoodNamesSpace.MapFoodFoodPortionType.ID)
        self.food_id = data.get(FoodNamesSpace.MapFoodFoodPortionType.FOOD_ID)
        self.food_portion_type_id = data.get(FoodNamesSpace.MapFoodFoodPortionType.FOOD_PORTION_TYPE_ID)
        self.create_user_id = data.get(FoodNamesSpace.MapFoodFoodPortionType.CREATE_USER_ID)

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