from django.db import models
from django.contrib.auth.models import User
from affiliates.models import ProductLinks

# Create your models here.

class UserDetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    phone=models.CharField(max_length=10,null=True)
    age=models.IntegerField(null=True)
    creds=models.IntegerField(default=0)

class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product_id=models.ForeignKey(ProductLinks,on_delete=models.DO_NOTHING)
    order_id=models.AutoField(primary_key=True)
    order_creds=models.IntegerField(default=0)