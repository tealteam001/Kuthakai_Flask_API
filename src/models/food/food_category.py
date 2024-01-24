
from src.db import db
from ...utils import NameSpace
from sqlalchemy import func

FoodNamesSpace = NameSpace.Schemas.FoodSchema
UserNamesSpace = NameSpace.Schemas.UserSchema

class FoodCategoryModel(db.Model):
    __tablename__ = FoodNamesSpace.FoodCategory.TABLE_NAME
    __table_args__ = { "schema":FoodNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    food_category = db.Column(db.String(128), nullable=False, unique=True)
    description = db.Column(db.String(256), nullable=False)
    create_user_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.User.TABLE_NAME}.{UserNamesSpace.User.ID}"),nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, onupdate=func.now())
    foods = db.relationship("FoodModel", back_populates="food_categories", secondary= f"{FoodNamesSpace.SCHEMA_NAME}.{FoodNamesSpace.MapFoodFoodCategory.TABLE_NAME}")

    def __init__(self, data):
        id = data.get(FoodNamesSpace.FoodCategory.ID)
        self.food_category = data.get(FoodNamesSpace.FoodCategory.FOOD_CATEGORY)
        self.description = data.get(FoodNamesSpace.FoodCategory.DESCRIPTION)
        self.create_user_id = data.get(FoodNamesSpace.FoodCategory.CREATE_USER_ID)
        self.created_at = data.get(FoodNamesSpace.FoodCategory.CREATED_BY)
        self.updated_at = data.get(FoodNamesSpace.FoodCategory.UPDATED_BY)

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






