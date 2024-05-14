from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Userblog(models.Model):

    CAT=(
        ("World","World"),
        ("Tech","Tech"),
        ("Business","Business"),
        ("Art-Design","Art-Design"),
        ("Entertainment","Entertainment")
    )

    bname=models.CharField(max_length=100,verbose_name="bloger name")
    buid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="buid",verbose_name="bloger id")
    bcat=models.CharField(max_length=100,verbose_name="category", choices=CAT)
    btitle=models.CharField(max_length=500,verbose_name="title")
    bdate=models.DateField(default=datetime.datetime.now(),verbose_name="date")
    bimages=models.ImageField(upload_to='userblogs',verbose_name="Images")
    bshort_description=models.CharField(max_length=999,verbose_name="shortdesc")
    bdescription=models.CharField(max_length=9999,verbose_name="description")


    def __str__(self):
        return self.bname