from src.db import db
from ...utils import NameSpace

UserNamesSpace = NameSpace.Schemas.UserSchema

class UserTypeModel(db.Model):
    __tablename__ = UserNamesSpace.UserType.TABLE_NAME
    __table_args__ = { "schema":UserNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(128),unique=True, nullable=False)
    description = db.Column(db.String(256), nullable=False)
    users = db.relationship("UserModel", back_populates="user_type", lazy="dynamic")

    def __init__(self, data):
        id = data.get(UserNamesSpace.UserType.ID)
        self.type = data.get(UserNamesSpace.UserType.TYPE)
        self.description = data.get(UserNamesSpace.UserType.DESCRIPTION)

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





