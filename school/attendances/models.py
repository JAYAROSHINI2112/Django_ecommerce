from django.db import models

# Create your models here.
class attendclassmaster(models.Model):
    classid = models.IntegerField()
    classname = models.IntegerField()
    data = models.DateField(editable=False)