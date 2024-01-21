from src.db import db
from ...utils import NameSpace
from sqlalchemy import func

FoodNamesSpace = NameSpace.Schemas.FoodSchema
UserNamesSpace = NameSpace.Schemas.UserSchema


class MapFoodFoodCategoryModel(db.Model):
    __tablename__ = FoodNamesSpace.MapFoodFoodCategory.TABLE_NAME
    __table_args__ = { "schema":FoodNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey(f"{FoodNamesSpace.SCHEMA_NAME}.{FoodNamesSpace.Food.TABLE_NAME}.{FoodNamesSpace.Food.ID}"),nullable=False)
    food_category_id = db.Column(db.Integer,db.ForeignKey(f"{FoodNamesSpace.SCHEMA_NAME}.{FoodNamesSpace.FoodCategory.TABLE_NAME}.{FoodNamesSpace.FoodCategory.ID}"),nullable=False)
    create_user_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.User.TABLE_NAME}.{UserNamesSpace.User.ID}"),nullable=False)
    created_at = db.Column(db.DateTime, nullbale=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullbale=False, onupdate=func.now())

    def __init__(self, data):
        id = data.get(FoodNamesSpace.MapFoodFoodCategory.ID)
        self.food_id = data.get(FoodNamesSpace.MapFoodFoodCategory.FOOD_ID)
        self.food_category_id = data.get(FoodNamesSpace.MapFoodFoodCategory.FOOD_CATEGORY_ID)
        self.create_user_id = data.get(FoodNamesSpace.MapFoodFoodCategory.CREATE_USER_ID)
        self.created_at = data.get(FoodNamesSpace.MapFoodFoodCategory.CREATED_BY)
        self.updated_at = data.get(FoodNamesSpace.MapFoodFoodCategory.UPDATED_BY)

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