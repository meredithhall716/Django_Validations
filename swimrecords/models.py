from datetime import timedelta
from django.utils import timezone
from logging import raiseExceptions
from xml.dom import ValidationErr
from django.forms import ValidationError
from django.db import models


def relay_check(stroke):
    # 'front crawl', 'butterfly', 'breast', 'back', or 'freestyle
    stroke_list = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if stroke not in stroke_list:
        raise ValidationError(f"{stroke} is not a valid stroke")


def distance_check(distance):
    limit = 50
    if distance <= limit:
        raise ValidationError(
            "Ensure this value is greater than or equal to 50.")


def date_check(date):
    if date > timezone.now():
        raise ValidationError("Can't set record in the future.")


def record_broken_date_check(record_broken_date):
    if record_broken_date < timezone.now():
        raise ValidationError("Can't break record before record was set.")
    return record_broken_date


class SwimRecord(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255)
    relay = models.BooleanField(default=False)
    stroke = models.CharField(max_length=255, validators=[relay_check])
    distance = models.IntegerField(validators=[distance_check])
    record_date = models.DateTimeField(validators=[date_check])
    record_broken_date = models.DateTimeField(
        validators=[record_broken_date_check])
