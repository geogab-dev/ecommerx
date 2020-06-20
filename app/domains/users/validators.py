from app.domains.users.exceptions import InvalidNameException, InvalidEmailException
import re


def is_user_name_valid(name):
    if not bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', string=str(name))):
        raise InvalidNameException(name=name)


def is_user_email_valid(email):
    if not bool(re.fullmatch(r"^[^\s@<>\(\)\[\]\.]+(?:\.[^\s@<>\(\)\[\]\.]+)*@\w+(:?[\.\-\_]\w+)*$", string=str(email))):
        raise InvalidEmailException(email=email)
