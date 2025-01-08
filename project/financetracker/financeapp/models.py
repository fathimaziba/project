from django.db import models

# Create your models here.


class user(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=15)
    phonenumber=models.CharField(max_length=10)
    
class transaction(models.Model):
    amount=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    date=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
