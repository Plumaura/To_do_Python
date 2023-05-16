from django.db import models

# Create your models here.

class Users(models.Model):
    """
    This module is about users where exist in DB.
    in private parameter : userName & userId & userPwd
    """
    userName = models.CharField(max_length=10)
    userId = models.CharField(max_length=10)
    userPw = models.CharField(max_length=20)
    