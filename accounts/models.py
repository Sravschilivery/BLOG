from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    mob_no=models.IntegerField()
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    uimg=models.ImageField(upload_to="profile")
    uadd=models.CharField(max_length=555)
