from django.db import models


# Create your models here.

"""
    
"""
class UserInfo(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=32, unique=True)
    title = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class UserPWD(models.Model):
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE, primary_key=True)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.user.name

