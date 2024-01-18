from src.db import db
from ...utils import NameSpace

CustomerNamesSpace = NameSpace.Schemas.CustomerSchema
UserNamesSpace = NameSpace.Schemas.UserSchema

class CustomerModel(db.Model):
    __tablename__ = CustomerNamesSpace.Customer.TABLE_NAME
    __table_args__ = { "schema":CustomerNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(256), nullable=False)
    user_name = db.Column(db.String(256), unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    phone_number= db.Column(db.String, nullable=False)
    create_user_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.User.TABLE_NAME}.{UserNamesSpace.User.ID}"),nullable=False)
    orders = db.relationship("CustomerModel", back_populates="customer", lazy="dynamic")

    def __init__(self, data):
        id = data.get(CustomerNamesSpace.Customer.ID)
        self.address = data.get(CustomerNamesSpace.Customer.ADDRESS)
        self.user_name = data.get(CustomerNamesSpace.Customer.USER_NAME)
        self.email = data.get(CustomerNamesSpace.Customer.EMAIL)
        self.password = data.get(CustomerNamesSpace.Customer.PASSWORD)
        self.phone_number = data.get(CustomerNamesSpace.Customer.PHONE_NUMBER)
        self.create_user_id = data.get(CustomerNamesSpace.Customer.CREATE_USER_ID)

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



