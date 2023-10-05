from django.db import models

# Create your models here.
class Bug(models.Model):
    """This defines the bug db model"""

    description = models.CharField(max_length=200)
    bug_type = models.CharField(max_length=200)
    report_date = models.DateTimeField("report date")
    status = models.CharField(max_length=200)
	
