from src.db import db
from ...utils import NameSpace

OrderNamesSpace = NameSpace.Schemas.OrderSchema

class OrderTypeModel(db.Model):
    __tablename__ = OrderNamesSpace.OrderType.TABLE_NAME
    __table_args__ = { "schema":OrderNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80),unique=True,  nullable=False)
    description = db.Column(db.String(256), nullable=False)
    orders = db.relationship("OrderModel", back_populates="order_type", lazy="dynamic")

    def __init__(self, data):
        id = data.get(OrderNamesSpace.OrderType.ID)
        self.type = data.get(OrderNamesSpace.OrderType.TYPE)
        self.description = data.get(OrderNamesSpace.OrderType.DESCRIPTION)

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





