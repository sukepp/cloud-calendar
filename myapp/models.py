import django.utils.timezone as timezone
from django.db import models
from django.db.models import CharField, DateField, ForeignKey, IntegerField, TimeField
from django.contrib.auth.models import User

# Create your models here.

# Create your models here.
EVENT_TYPE = (('active', 'active'), ('old', 'old'))


class Record(models.Model):
    date = DateField()
    time_start = models.TimeField(auto_now=False, auto_now_add=False, default='00:00')
    time_end = models.TimeField(auto_now=False, auto_now_add=False, default='00:00')
    title = CharField(max_length=300)
    description = CharField(max_length=300)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    event_type = CharField(max_length=8, choices=EVENT_TYPE)

    def __str__(self):
        return self.description
