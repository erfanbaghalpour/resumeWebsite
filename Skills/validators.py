from django.core.validators import ValidationError


def max_value_validator(value):
    if value > 100:
        raise ValidationError("The value which is entered is greater than the limit")


def min_value_validator(value):
    if value < 0:
        raise ValidationError("The value which is entered is less than the limit")
