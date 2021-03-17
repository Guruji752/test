from django.db import models
from datetime import datetime
# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.IntegerField()
    contact=models.CharField(max_length=20)
    def __str__(self):
        return self.first_name