from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.name

class products(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Home/images' ,null=True,blank=True)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, null=True,blank=True,on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return self.name
