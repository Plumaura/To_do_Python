from django.contrib.auth.models import AbstractBaseUser
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


class TestUser(models.Model):
    userNum = models.IntegerField(primary_key=True)
    userId = models.CharField(max_length=10)
    userPw = models.CharField(max_length=20)
    userName = models.CharField(max_length=10)

class TestList(models.Model):
    listNum = models.AutoField(primary_key=True)
    userNum = models.ForeignKey(TestUser, on_delete=models.CASCADE, db_column='userNum')
    listTitle = models.CharField(max_length=50)
    listContent = models.TextField()
    listCheck = models.IntegerField()




# class myUser(models.Model):
#     """
#     This module is about users where exist in DB.
#     in private parameter : userName & userId & userPwd
#     """
#     userNum = models.IntegerField(primary_key=True) # 학번
#     userId = models.CharField(max_length=10)
#     userPw = models.CharField(max_length=20)
#     userName = models.CharField(max_length=10) # 닉네임

# class myList(models.Model):
#     """
#     This module is about users where exist in DB.
#     in private parameter : userName & userId & userPwd
#     """
#     listNum = models.AutoField(primary_key=True)
#     userNum = models.CharField(max_length=10) # 외래키 (userName 불러오기)
#     listTitle = models.CharField(max_length=50)
#     listContent = models.CharField(max_length=20)
#     listCheck = models.IntegerField() # To인지 Do인지 체크 (0 or 1)


# class TestUser(AbstractBaseUser):
#     """
#     This module is about users where exist in DB.
#     in private parameter : userName & userId & userPwd
#     """
#     userNum = models.IntegerField(primary_key=True)
#     userId = models.CharField(max_length=10, unique=True)
#     userPw = models.CharField(max_length=20)
#     userName = models.CharField(max_length=10)

#     USERNAME_FIELD = 'userId'
#     REQUIRED_FIELDS = ['userName']