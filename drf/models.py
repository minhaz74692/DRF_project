from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=25)
    user_id = models.CharField(max_length=20)
    age = models.IntegerField()
    profession = models.CharField(max_length=25)
