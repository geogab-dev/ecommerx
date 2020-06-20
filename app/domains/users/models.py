import datetime
import uuid

from app.domains.users.validators import is_user_name_valid, is_user_email_valid
from database import db


class Users(db.Document):
    _id = db.StringField(default=str(uuid.uuid4()), primary_key=True)
    name = db.StringField(required=True, validation=is_user_name_valid)
    last_name = db.StringField(required=True, validation=is_user_name_valid)
    email = db.StringField(required=True, validation=is_user_email_valid)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow())
    updated_at = db.DateTimeField(default=datetime.datetime.utcnow())

    def serialize(self):
        return {
            "_id": self._id,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
