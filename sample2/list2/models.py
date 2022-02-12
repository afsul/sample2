from django.db import models


# Create your models here.

class list2(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.IntegerField()
    age=models.IntegerField()

    
  
