from src.db import db
from ...utils import NameSpace

OrderNamesSpace = NameSpace.Schemas.OrderSchema
UserNamesSpace = NameSpace.Schemas.UserSchema

class OrderModel(db.Model):
    __tablename__ = OrderNamesSpace.Order.TABLE_NAME
    __table_args__ = { "schema":OrderNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    #customer_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.User.TABLE_NAME}.{UserNamesSpace.User.ID}"),nullable=False)
    description = db.Column(db.String(80),nullable=True)
    #requested_time = db.Column(db.T, nullable=False)
    supplier_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.User.TABLE_NAME}.{UserNamesSpace.User.ID}"),nullable=False)
    create_user_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.User.TABLE_NAME}.{UserNamesSpace.User.ID}"),nullable=True)
    order_type_id = db.Column(db.Integer,db.ForeignKey(f"{OrderNamesSpace.SCHEMA_NAME}.{OrderNamesSpace.OrderType.TABLE_NAME}.{OrderNamesSpace.OrderType.ID}"),nullable=False)
    discount_type_id = db.Column(db.Integer,db.ForeignKey(f"{OrderNamesSpace.SCHEMA_NAME}.{OrderNamesSpace.DiscountType.TABLE_NAME}.{OrderNamesSpace.DiscountType.ID}"),nullable=False)
    order_status_id = db.Column(db.Integer,db.ForeignKey(f"{OrderNamesSpace.SCHEMA_NAME}.{OrderNamesSpace.OrderStatus.TABLE_NAME}.{OrderNamesSpace.OrderStatus.ID}"),nullable=False)
    supplier = db.relationship("UserModel", back_populates="users")
    order_type = db.relationship("OrderTypeModel", back_populates="orders")
    order_status = db.relationship("OrderStatusModel", back_populates="orders")
    discount_type = db.relationship("DiscountTypeModel", back_populates="orders")
    customer = db.relationship("CustomerModel", back_populates="customers")

    def __init__(self, data):
        id = data.get(OrderNamesSpace.Order.ID)
        self.customer_id = data.get(OrderNamesSpace.Order.CUSTOMER_ID)
        self.description = data.get(OrderNamesSpace.Order.DESCRIPTION)
        self.requested_time = data.get(OrderNamesSpace.Order.REQUESTED_TIME)
        self.supplier_id = data.get(OrderNamesSpace.Order.SUPPLIER_ID)
        self.create_user_id = data.get(OrderNamesSpace.Order.CREATE_USER_ID)
        self.order_type_id= data.get(OrderNamesSpace.Order.ORDER_TYPE_ID)
        self.discount_type_id= data.get(OrderNamesSpace.Order.DISCOUNT_TYPE_ID)
        self.order_status_id= data.get(OrderNamesSpace.Order.ORDER_STATUS_ID)

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
