from src.db import db
from ...utils import NameSpace
from sqlalchemy import func

OrderNamesSpace = NameSpace.Schemas.OrderSchema
FoodNamesSpace = NameSpace.Schemas.FoodSchema
UserNamesSpace = NameSpace.Schemas.UserSchema

class MapOrderFoodModel(db.Model):
    __tablename__ = OrderNamesSpace.MapOrderFood.TABLE_NAME
    __table_args__ = { "schema":OrderNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey(f"{FoodNamesSpace.SCHEMA_NAME}.{FoodNamesSpace.Food.TABLE_NAME}.{FoodNamesSpace.Food.ID}"),nullable=False)
    order_id = db.Column(db.Integer,db.ForeignKey(f"{OrderNamesSpace.SCHEMA_NAME}.{OrderNamesSpace.Order.TABLE_NAME}.{OrderNamesSpace.Order.ID}"),nullable=False)
    count = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, onupdate=func.now())

    def __init__(self, data):
        id = data.get(OrderNamesSpace.MapOrderFood.ID)
        self.food_id = data.get(OrderNamesSpace.MapOrderFood.FOOD_ID)
        self.order_id = data.get(OrderNamesSpace.MapOrderFood.ORDER_ID)
        self.count = data.get(OrderNamesSpace.MapOrderFood.COUNT)
        self.create_user_id = data.get(UserNamesSpace.User.CREATE_USER_ID)
        self.created_at = data.get(OrderNamesSpace.MapOrderFood.CREATED_BY)
        self.updated_at = data.get(OrderNamesSpace.MapOrderFood.UPDATED_BY)

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