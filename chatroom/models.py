from django.db import models

# Create your models here.
class Messages(models.Model):
    name = models.CharField(max_length=20)
    message = models.CharField(max_length=100)

