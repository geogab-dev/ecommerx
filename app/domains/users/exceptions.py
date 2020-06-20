from app.exceptions import BadRequestException, UnprocessableException, NotFoundException


class ValidationErrorException(BadRequestException):
    def __init__(self):
        msg: str = "ValidationError, please check if all fields are filled correctly."
        super().__init__(msg=msg)


class InvalidNameException(UnprocessableException):
    def __init__(self, name):
        msg: str = f"{name} is not a valid name, please try again."
        super().__init__(msg=msg)


class InvalidEmailException(UnprocessableException):
    def __init__(self, email):
        msg: str = f"{email} is not a valid email, please try again."
        super().__init__(msg=msg)


class UserNotFoundException(NotFoundException):
    def __init__(self, id_user):
        msg: str = f"user ID: {id_user} not found."
        super().__init__(msg=msg)
