from django.db import models

# Create your models here.
class Team(models.Model):
    name=models.CharField(max_length=300)
    qualification=models.TextField()
    image=models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name




class Contact(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    message=models.TextField()


    def __str__(self):
        return self.first_name


class Create_Course(models.Model):
    name=models.CharField(max_length=300)
    qualification=models.CharField(max_length=300)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    content=models.CharField(max_length=300)
    course_video=models.FileField()


    def __str__(self):
        return self.name


class Upload_Content(models.Model):
    name=models.CharField(max_length=300)
    qualification=models.CharField(max_length=300)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    content=models.TextField()


    def __str__(self):
        return self.name