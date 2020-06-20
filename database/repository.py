import datetime

from database import db


def save(model: db.Document):
    model.save()
    return model


def update(model: db.Document, data: dict):
    model.update(**data, updated_at=datetime.datetime.utcnow())
    return save(model)


def delete(model: db.Document):
    model.delete()
    save(model)
