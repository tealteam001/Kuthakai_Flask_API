
from src.db import db
from ...utils import NameSpace

FoodNamesSpace = NameSpace.Schemas.FoodSchema
UserNamesSpace = NameSpace.Schemas.UserSchema

class FoodCategoryModel(db.Model):
    __tablename__ = FoodNamesSpace.FoodCategory.TABLE_NAME
    __table_args__ = { "schema":FoodNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    food_category = db.Column(db.String(256), nullable=False)
    create_user_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.User.TABLE_NAME}.{UserNamesSpace.User.ID}"),nullable=False)
    foods = db.relationship("FoodModel", back_populates="food_categories", secondary="map_food_food_category")

    def __init__(self, data):
        id = data.get(FoodNamesSpace.FoodCategory.ID)
        self.food_category = data.get(FoodNamesSpace.FoodCategory.FOOD_CATEGORY)
        self.create_user_id = data.get(FoodNamesSpace.FoodCategory.CREATE_USER_ID)

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






