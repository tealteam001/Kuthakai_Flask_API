
from src.db import db
from ...utils import NameSpace
from sqlalchemy import func

FoodNamesSpace = NameSpace.Schemas.FoodSchema
UserNamesSpace = NameSpace.Schemas.UserSchema
OrderNamesSpace = NameSpace.Schemas.OrderSchema

class FoodModel(db.Model):
    __tablename__ = FoodNamesSpace.Food.TABLE_NAME
    __table_args__ = { "schema":FoodNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(128),unique=True, nullable=False)
    description = db.Column(db.String(256), nullable=False)
    create_user_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.User.TABLE_NAME}.{UserNamesSpace.User.ID}"),nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, onupdate=func.now())
    food_categories = db.relationship("FoodCategoryModel", back_populates="foods", secondary=f"{FoodNamesSpace.SCHEMA_NAME}.{FoodNamesSpace.MapFoodFoodCategory.TABLE_NAME}")
    food_portion_types = db.relationship("FoodPortionTypeModel", back_populates="foods", secondary=f"{FoodNamesSpace.SCHEMA_NAME}.{FoodNamesSpace.MapFoodFoodPortionType.TABLE_NAME}")
    orders = db.relationship("OrderModel", back_populates="foods", secondary=f"{OrderNamesSpace.SCHEMA_NAME}.{OrderNamesSpace.MapOrderFood.TABLE_NAME}")


    def __init__(self, data):
        id = data.get(FoodNamesSpace.Food.ID)
        self.price = data.get(FoodNamesSpace.Food.PRICE)
        self.name = data.get(FoodNamesSpace.Food.NAME)
        self.description = data.get(FoodNamesSpace.Food.DESCRIPTION)
        self.create_user_id = data.get(FoodNamesSpace.Food.CREATE_USER_ID)
        self.created_at = data.get(FoodNamesSpace.Food.CREATED_BY)
        self.updated_at = data.get(FoodNamesSpace.Food.UPDATED_BY)

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






