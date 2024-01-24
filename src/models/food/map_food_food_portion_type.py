from src.db import db
from ...utils import NameSpace
from sqlalchemy import func

FoodNamesSpace = NameSpace.Schemas.FoodSchema
UserNamesSpace = NameSpace.Schemas.UserSchema


class MapFoodFoodPortionTypeModel(db.Model):
    __tablename__ = FoodNamesSpace.MapFoodFoodPortionType.TABLE_NAME
    __table_args__ = { "schema":FoodNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey(f"{FoodNamesSpace.SCHEMA_NAME}.{FoodNamesSpace.Food.TABLE_NAME}.{FoodNamesSpace.Food.ID}"),nullable=False)
    food_portion_type_id = db.Column(db.Integer,db.ForeignKey(f"{FoodNamesSpace.SCHEMA_NAME}.{FoodNamesSpace.FoodProtionType.TABLE_NAME}.{FoodNamesSpace.FoodProtionType.ID}"),nullable=False)
    create_user_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.User.TABLE_NAME}.{UserNamesSpace.User.ID}"),nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, onupdate=func.now())

    def __init__(self, data):
        id = data.get(FoodNamesSpace.MapFoodFoodPortionType.ID)
        self.food_id = data.get(FoodNamesSpace.MapFoodFoodPortionType.FOOD_ID)
        self.food_portion_type_id = data.get(FoodNamesSpace.MapFoodFoodPortionType.FOOD_PORTION_TYPE_ID)
        self.create_user_id = data.get(FoodNamesSpace.MapFoodFoodPortionType.CREATE_USER_ID)
        self.created_at = data.get(FoodNamesSpace.MapFoodFoodPortionType.CREATED_BY)
        self.updated_at = data.get(FoodNamesSpace.MapFoodFoodPortionType.UPDATED_BY)

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