from src.db import db
from ...utils import NameSpace

OrderNamesSpace = NameSpace.Schemas.OrderSchema

class OrderFoodStatusModel(db.Model):
    __tablename__ = OrderNamesSpace.OrderFoodStatus.TABLE_NAME
    __table_args__ = { "schema":OrderNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(80),unique=True, nullable=False )
    description = db.Column(db.String(256), nullable=False)
    order_foods = db.relationship("OrderFoodModel", back_populates="order_food_status", lazy="dynamic")

    def __init__(self, data):
        id = data.get(OrderNamesSpace.OrderFoodStatus.ID)
        self.status = data.get(OrderNamesSpace.OrderFoodStatus.STATUS)
        self.description = data.get(OrderNamesSpace.OrderFoodStatus.DESCRIPTION)

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





