from django.db import models

# Create your models here.

class classesregister(models.Model):
    cclass=models.IntegerField(unique=True,blank=True,null=True)
    
    def __str__(self):
        return f'Class: {str(self.cclass)}'
