import datetime
import re
from django.core.exceptions import ValidationError
# from users.models import User


def validate_username(value):
    if re.search(r'^[\w.@+-]+$', value) is None:
        raise ValidationError(('Username has unallowed symbols'),)
    if value == 'me':
        raise ValidationError(('You cant use me as username'),)


"""def validate_email(self, value):
    if User.objects.filter(email=value).exists():
        raise ValidationError('Email is already in use')"""


def validate_custom_year(value):
    if value > datetime.datetime.now().year:
        raise ValidationError(
            f'Year cant be more than {datetime.datetime.now().year}'
        )
