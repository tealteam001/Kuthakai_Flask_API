from src.db import db
from ...utils import NameSpace
from sqlalchemy import func

CustomerNamesSpace = NameSpace.Schemas.CustomerSchema
UserNamesSpace = NameSpace.Schemas.UserSchema

class CustomerModel(db.Model):
    __tablename__ = CustomerNamesSpace.Customer.TABLE_NAME
    __table_args__ = { "schema":CustomerNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(256), nullable=True)
    user_name = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    phone_number= db.Column(db.Integer, nullable=False)
    create_user_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.User.TABLE_NAME}.{UserNamesSpace.User.ID}"),nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, onupdate=func.now())
    orders = db.relationship("CustomerModel", back_populates="customer", lazy="dynamic")

    def __init__(self, data):
        id = data.get(CustomerNamesSpace.Customer.ID)
        self.address = data.get(CustomerNamesSpace.Customer.ADDRESS)
        self.user_name = data.get(CustomerNamesSpace.Customer.USER_NAME)
        self.email = data.get(CustomerNamesSpace.Customer.EMAIL)
        self.password = data.get(CustomerNamesSpace.Customer.PASSWORD)
        self.phone_number = data.get(CustomerNamesSpace.Customer.PHONE_NUMBER)
        self.create_user_id = data.get(CustomerNamesSpace.Customer.CREATE_USER_ID)
        self.created_at = data.get(CustomerNamesSpace.Customer.CREATED_BY)
        self.updated_at = data.get(CustomerNamesSpace.Customer.UPDATED_BY)

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



