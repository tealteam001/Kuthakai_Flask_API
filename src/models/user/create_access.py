from src.db import db
from ...utils import NameSpace
from sqlalchemy import func

UserNamesSpace = NameSpace.Schemas.UserSchema

class CreateAccessModel(db.Model):
    __tablename__ = UserNamesSpace.CreateAccess.TABLE_NAME
    __table_args__ = { "schema":UserNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    privilage_entity_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.PrivilageEntity.TABLE_NAME}.{UserNamesSpace.PrivilageEntity.ID}"), nullable=False)
    create_user_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.User.TABLE_NAME}.{UserNamesSpace.User.ID}"), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey(f"{UserNamesSpace.SCHEMA_NAME}.{UserNamesSpace.User.TABLE_NAME}.{UserNamesSpace.User.ID}"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, onupdate=func.now())
    user = db.relationship("UserModel", back_populates="create_accesses")
    privilage_entity = db.relationship("PrivilageEntityModel", back_populates="create_accesses")


    def __init__(self, data):
        id = data.get(UserNamesSpace.CreateAccess.ID)
        self.privilage_entity_id = data.get(UserNamesSpace.CreateAccess.PRIVILAGE_ENTITY_ID)
        self.create_user_id = data.get(UserNamesSpace.CreateAccess.CREATE_USER_ID)
        self.user_id = data.get(UserNamesSpace.CreateAccess.USER_ID)
        self.created_at = data.get(UserNamesSpace.CreateAccess.CREATED_BY)
        self.updated_at = data.get(UserNamesSpace.CreateAccess.UPDATED_BY)
        user = db.relationship("UserModel", back_populates="create_accesses")

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





