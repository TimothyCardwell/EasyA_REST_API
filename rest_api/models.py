from django.db import models

# Create your models here.


# TODO This hasn't been migrated yet
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()