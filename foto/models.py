from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

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

