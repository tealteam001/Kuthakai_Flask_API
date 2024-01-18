from src.db import db
from ...utils import NameSpace

OrderNamesSpace = NameSpace.Schemas.OrderSchema

class OrderStatusModel(db.Model):
    __tablename__ = OrderNamesSpace.OrderStatus.TABLE_NAME
    __table_args__ = { "schema":OrderNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(80), nullable=False)
    orders = db.relationship("OrderModel", back_populates="order_status", lazy="dynamic")

    def __init__(self, data):
        id = data.get(OrderNamesSpace.OrderStatus.ID)
        self.status = data.get(OrderNamesSpace.OrderStatus.STATUS)

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





