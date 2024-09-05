from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.




class profile(models.Model):
    user=models.OneToOneField(User,primary_key=True,on_delete=models.CSACADE)
    avater=models.ImageField(null=True,default="static\doctor.jpg")

    


"""class iamuser(AbstractUser):
    username=None
    email=models.EmailField(null=False,unique=True, max_length=254)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []"""


class dataset(models.Model):
    path=models.CharField(null=False,max_length=100)
    date=models.DateTimeField(null=False)
    event=models.CharField(null=True,max_length=50)
    name=models.CharField(null=True,max_length=50)
    likes=models.IntegerField(null=True,default=0)

