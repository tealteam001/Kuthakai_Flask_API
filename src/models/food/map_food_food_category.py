from src.db import db
from ...utils import NameSpace

FoodNamesSpace = NameSpace.Schemas.FoodSchema


class MapFoodFoodCategory(db.Model):
    __tablename__ = FoodNamesSpace.MapFoodFoodCategory.TABLE_NAME
    __table_args__ = { "schema":FoodNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey(f"{FoodNamesSpace.SCHEMA_NAME}.{FoodNamesSpace.Food.TABLE_NAME}.{FoodNamesSpace.Food.ID}"),nullable=False)
    food_category_id = db.Column(db.Integer,db.ForeignKey(f"{FoodNamesSpace.SCHEMA_NAME}.{FoodNamesSpace.FoodCategory.TABLE_NAME}.{FoodNamesSpace.FoodCategory.ID}"),nullable=False)

    def __init__(self, data):
        id = data.get(FoodNamesSpace.MapFoodFoodCategory.ID)
        self.food_id = data.get(FoodNamesSpace.MapFoodFoodCategory.FOOD_ID)
        self.food_category_id = data.get(FoodNamesSpace.MapFoodFoodCategory.FOOD_CATEGORY_ID)
        self.create_user_id = data.get(FoodNamesSpace.MapFoodFoodCategory.CREATE_USER_ID)

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