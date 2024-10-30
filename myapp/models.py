from django.db import models

# Create your models here.
class usermodel(models.Model):
    username=models.CharField(max_length=100)
    user_date=models.DateField()
    user_age=models.IntegerField()
class mediause(models.Model):
    name =models.CharField(max_length=20)
    place = models.CharField(max_length=40)
    image = models.ImageField(upload_to='imgaes/')

from django.contrib.auth.models import AbstractUser

class Customuser(AbstractUser):
    bio = models.TextField()
    pr_pic = models.ImageField(upload_to="img/")   
    dob = models.DateField() 

    