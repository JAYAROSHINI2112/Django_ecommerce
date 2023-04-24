from django.db import models

# Create your models here.
class attendclassmaster(models.Model):
    classid = models.IntegerField()
    classname = models.IntegerField()
    data = models.DateField(editable=False)


class attendanceentry(models.Model):
    studid = models.IntegerField()
    classid = models.IntegerField()
    dateid = models.IntegerField()
    pafield = models.BooleanField()