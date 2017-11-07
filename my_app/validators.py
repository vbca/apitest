from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

def validate_date_event(value):
    if value <= datetime.now().date():
        raise ValidationError(
            _("la fecha no puede ser menor o igual a la del día de hoy"),
            params={'value': value},
        )

def age_validation(value):
    '''Age validation for user input'''
    if value < 21:
        raise ValidationError(
            _("Debes de ser mayor de edad"),
            params={"value":value},
        )
