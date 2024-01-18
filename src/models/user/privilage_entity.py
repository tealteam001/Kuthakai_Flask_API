from src.db import db
from ...utils import NameSpace

UserNamesSpace = NameSpace.Schemas.UserSchema

class PrivilageEntityModel(db.Model):
    __tablename__ = UserNamesSpace.PrivilageEntity.TABLE_NAME
    __table_args__ = { "schema":UserNamesSpace.SCHEMA_NAME}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    create_accesses = db.relationship("CreateAccessModel", back_populates="privilage_entity", lazy="dynamic")
    edit_accesses = db.relationship("EditAccessModel", back_populates="privilage_entity", lazy="dynamic")
    delete_accesses = db.relationship("DeleteAccessModel", back_populates="privilage_entity", lazy="dynamic")
    veiw_accesses = db.relationship("VeiwAccessModel", back_populates="privilage_entity", lazy="dynamic")

    def __init__(self, data):
        id = data.get(UserNamesSpace.PrivilageEntity.ID)
        self.name = data.get(UserNamesSpace.PrivilageEntity.NAME)

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





