import datetime

from django.core.exceptions import ValidationError


def validate_custom_year(value):
    if value > datetime.datetime.now().year:
        raise ValidationError(
            f'Год не может быть больше {datetime.datetime.now().year}'
        )
