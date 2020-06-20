from database.repository import save, update, db, delete
from app.domains.users.models import Users
from app.domains.users.exceptions import ValidationErrorException, UserNotFoundException


def get_all_users():
    return Users.objects


def get_user_by_id(id_user: str):
    try:
        return Users.objects.get(_id=id_user)
    except db.DoesNotExist:
        raise UserNotFoundException(id_user=id_user)


def insert_user(data: dict):
    try:
        user = Users(**data)
        return save(user)
    except db.ValidationError:
        raise ValidationErrorException()


def update_user(id_user: str, data: dict):
    try:
        user = get_user_by_id(id_user=id_user)
        return update(model=user, data=data)
    except db.InvalidQueryError:
        raise ValidationErrorException()


def delete_user(id_user: str):
    user = get_user_by_id(id_user=id_user)
    delete(user)
