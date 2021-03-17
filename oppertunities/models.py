from django.db import models

# Create your models here.
class Writing(models.Model):
    title=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='opertunities/')
    description=models.TextField()
    

    def __str__(self):
        return self.title


class Translation(models.Model):
    title=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='opertunities/')
    description=models.TextField()

    def __str__(self):
        return self.title


class Research(models.Model):
    title=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='opertunities/')
    description=models.TextField()

    def __str__(self):
        return self.title



class HealthCare_OnlineConseltant(models.Model):
    title=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='opertunities/')
    description=models.TextField()

    def __str__(self):
        return self.title


class HealthCare_LiveSession(models.Model):
    title=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='opertunities/')
    description=models.TextField()

    def __str__(self):
        return self.title


class HealthCare_VideoLesson(models.Model):
    title=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='opertunities/')
    description=models.TextField()

    def __str__(self):
        return self.title

class HomeCare(models.Model):
    title=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='opertunities/')
    description=models.TextField()

    def __str__(self):
        return self.title