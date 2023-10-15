from django.db import models

# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()