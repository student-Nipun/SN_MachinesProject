from django.db import models
import datetime
# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=100,unique=True)
    product_describtion = models.CharField(max_length=300)
    product_link = models.CharField(max_length=500)
    product_img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.product_name


class Contact_Query(models.Model):
    name = models.CharField(max_length=60)
    mobileNo = models.CharField(max_length=15)
    requirements = models.CharField(max_length=600)
    date_time = models.DateTimeField(("Date"),default=datetime.datetime.today)
    def __str__(self):
        return self.name
    
    