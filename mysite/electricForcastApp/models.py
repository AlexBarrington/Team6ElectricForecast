from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserModel (models.Model):
    user = models.ForeignKey(User)
    username = models.TextField()
    email = models.TextField()
