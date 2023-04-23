from django.db import models

# Create your models here.

class teachersregister(models.Model):
    tname=models.CharField(max_length=200)
    tclass=models.ForeignKey("classes.classesregister",on_delete=models.CASCADE)
    tsession=models.CharField(max_length=10)
    tdate=models.DateTimeField(auto_now_add=True, editable=False)
    status=models.IntegerField(blank=True,default=1)

    def __str__(self):
        return self.tname
