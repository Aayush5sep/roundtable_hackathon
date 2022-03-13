from pyexpat import model
from django.db import models

# Create your models here.
class ProductLinks(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=100)
    price=models.CharField(max_length=10,default=0)
    affiliate_link=models.CharField(max_length=1000)
    webopt=(
        ("AMAZON","AMAZON"),
        ("FLIPKART","FLIPKART"),
        ("NYKAA","NYKAA"),
        ("SNAPDEAL","SNAPDEAL"),
        ("MESH","MESH"),
        ("OTHER","OTHER"),
    )
    website=models.CharField(max_length=25,choices=webopt,default="AMAZON")
    product_seller=models.CharField(max_length=100)
    influencer=models.CharField(max_length=50)
    image=models.CharField(max_length=1000,default="https://unsplash.com/photos/sxiSod0tyYQ")