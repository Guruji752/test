from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

# class User(AbstractUser):
# 	class Meta:
# 		db_table='auth_user'

class UserPersonalDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=100,null=True)

    class Meta:
    	db_table='user_details'