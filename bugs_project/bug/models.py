from django.db import models
from django.utils import timezone


class Bug(models.Model):
    """This defines the bug db model"""
    description = models.CharField(max_length=200)
    bug_type = models.CharField(max_length=200)
    report_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200)
