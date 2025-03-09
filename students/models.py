from django.db import models
from employee.models import employe

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    marks = models.FloatField()
    employe=models.ForeignKey(employe,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.name