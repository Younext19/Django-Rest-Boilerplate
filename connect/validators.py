import re
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UsernameValidator(validators.RegexValidator):
    regex = r'^[\w.-]+$'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and @/./+/-/_ characters.'
    )
    flags = 0


@deconstructible
class PhoneNumberValidator(validators.RegexValidator):
    regex = r'^\+?1?\d{9,15}$'
    message = _(
        "Phone number must be entered in the format: '+999999999999'. Up to 15 digits allowed."
    )
    flags = 0


@deconstructible
class EmailValidator(validators.RegexValidator):
    regex = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
    message = _(
        "Email must be entered in the format: 'example@example.example'."
    )
    flags = 0


def validate_phone_number(value):
    regex = r'^\+?1?\d{9,15}$'
    if value is not None:
        if re.search(regex, value):
            return True
        else:
            return False


def validate_email(value):
    regex = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
    if value is not None:
        if re.search(regex, value):
            return True
        else:
            return False


def validate_password(value):
    regex = r'[A-Za-z0-9@#$%^&+=].{8,20}$'
    if value is not None:
        if re.search(regex, value):
            return True
        else:
            return False


def validate_quantity(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is not a positive number'),
            params={'value': value},
        )
