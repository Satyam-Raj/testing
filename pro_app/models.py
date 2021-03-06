from django.db import models

# Create your models here.
class Something(models.Model):
    name        =       models.CharField(max_length=110)
    age         =       models.IntegerField()
    email       =       models.EmailField(max_length=100)
    description =       models.TextField()
    height      =       models.IntegerField()
    some_image  =       models.ImageField(null =True, blank=True, upload_to='images/')