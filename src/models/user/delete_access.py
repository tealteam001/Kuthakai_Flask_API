from src.db import db
from ...utils import NameSpace

UserNamesSpace = NameSpace.Schemas.UserSchema

class DeleteAccessModel(db.Model):
    __tablename__ = UserNamesSpace.DeleteAccess.TABLE_NAME
    __table_args__ = { "schema":UserNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    privilage_entity_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.PrivilageEntity.TABLE_NAME}.{UserNamesSpace.PrivilageEntity.ID}"), nullable=False)
    create_user_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.User.TABLE_NAME}.{UserNamesSpace.User.ID}"), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.User.TABLE_NAME}.{UserNamesSpace.User.ID}"), nullable=False)
    user = db.relationship("UserModel", back_populates="delete_accesses")
    privilage_entity = db.relationship("PrivilageEntityModel", back_populates="delete_accesses")

    def __init__(self, data):
        id = data.get(UserNamesSpace.DeleteAccess.ID)
        self.privilage_entity_id = data.get(UserNamesSpace.DeleteAccess.PRIVILAGE_ENTITY_ID)
        self.create_user_id = data.get(UserNamesSpace.DeleteAccess.CREATE_USER_ID)
        self.user_id = data.get(UserNamesSpace.DeleteAccess.USER_ID)

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





