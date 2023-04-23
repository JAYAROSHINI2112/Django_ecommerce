from django.db import models

# Create your models here.
class studentsregister(models.Model):
    sname=models.CharField(max_length=200)
    sclass=models.ForeignKey("classes.classesregister",on_delete=models.CASCADE)
    ssession=models.CharField(max_length=10)
    sdate=models.DateTimeField(auto_now_add=True, editable=False)
    status=models.IntegerField(blank=True,default=1)

    def __str__(self):
        return self.sname
    

