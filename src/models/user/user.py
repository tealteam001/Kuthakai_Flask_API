from src.db import db
from ...utils import NameSpace
from sqlalchemy import func

UserNamesSpace = NameSpace.Schemas.UserSchema

class UserModel(db.Model):
    __tablename__ = UserNamesSpace.User.TABLE_NAME
    __table_args__ = { "schema":UserNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    nic= db.Column(db.String(128), unique=True, nullable=False)
    create_user_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.User.TABLE_NAME}.{UserNamesSpace.User.ID}"),nullable=False)
    user_type_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.UserType.TABLE_NAME}.{UserNamesSpace.UserType.ID}"),nullable=False)
    created_at = db.Column(db.DateTime, nullbale=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullbale=False, onupdate=func.now())

    creator = db.relationship('UserModel', remote_side=[id], back_populates='users')
    users = db.relationship('UserModel', back_populates='creator', lazy='dynamic')

    user_type = db.relationship("UserTypeModel", back_populates="users")
    create_accesses = db.relationship("CreateAccessModel", back_populates="user", lazy="dynamic")
    edit_accesses = db.relationship("EditAccessModel", back_populates="user", lazy="dynamic")
    delete_accesses = db.relationship("DeleteAccessModel", back_populates="user", lazy="dynamic")
    veiw_accesses = db.relationship("VeiwAccessModel", back_populates="user", lazy="dynamic")

    def __init__(self, data):
        id = data.get(UserNamesSpace.User.ID)
        self.user_name = data.get(UserNamesSpace.User.USER_NAME)
        self.email = data.get(UserNamesSpace.User.EMAIL)
        self.password = data.get(UserNamesSpace.User.PASSWORD)
        self.nic= data.get(UserNamesSpace.User.NIC)
        self.create_user_id = data.get(UserNamesSpace.User.CREATE_USER_ID)
        self.user_type_id= data.get(UserNamesSpace.User.USER_TYPE_ID)
        self.created_at = data.get(UserNamesSpace.User.CREATED_BY)
        self.updated_at = data.get(UserNamesSpace.User.UPDATED_BY)

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
