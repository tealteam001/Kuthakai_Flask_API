from src.db import db
from ...utils import NameSpace

UserNamesSpace = NameSpace.Schemas.UserSchema

class CreateAccessModel(db.Model):
    __tablename__ = UserNamesSpace.CreateAccess.TABLE_NAME
    __table_args__ = { "schema":UserNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    privilage_entity_id = db.Column(db.Integer, nullable=False)
    create_user_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, data):
        id = data.get(UserNamesSpace.CreateAccess.ID)
        self.privilage_entity_id = data.get(UserNamesSpace.CreateAccess.PRIVILAGE_ENTITY_ID)
        self.create_user_id = data.get(UserNamesSpace.CreateAccess.CREATE_USER_ID)
        self.user_id = data.get(UserNamesSpace.CreateAccess.USER_ID)

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





