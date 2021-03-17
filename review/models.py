from django.db import models

# Create your models here.
class Review(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=500)
    feedback=models.TextField()
    is_publish=models.BooleanField(default=False)


    def __str__(self):
        return self.name
