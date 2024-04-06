from django.db import models
from django.contrib.auth.models import User
from product.models import product
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    product_favorit = models.ManyToManyField(product)
    #register the date plase 
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    #create function register the date resive from database
    def __str__(self):
        return self.user.username
