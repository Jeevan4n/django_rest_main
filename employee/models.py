from django.db import models

# Create your models here.
class employe(models.Model):
    emp_id=models.CharField(max_length=20,unique=True,primary_key=True)
    emp_name=models.CharField(max_length=100)
    role=models.CharField(max_length=30)
    salary=models.IntegerField()

    def __str__(self):
        return self.emp_name
