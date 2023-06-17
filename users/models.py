from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(verbose_name="name", max_length= 16 )
    pwd = models.CharField(verbose_name="password", max_length=64)
    mobile = models.CharField(verbose_name="mobile phone",max_length=64)
    email = models.CharField(verbose_name="email", max_length=32)
    age = models.IntegerField(verbose_name="age")
    subscribe = models.BooleanField(default=False)