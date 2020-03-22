from django.db import models

# Create your models here.
class employee(models.Model):
    Employee_code=models.CharField(max_length=100000,unique=True)
    Department=models.CharField(max_length=100)
    Score=models.IntegerField()
    Date_Created=models.DateTimeField()
def __str__(self):
    return f*{self.Employee_code} - {self.Department}