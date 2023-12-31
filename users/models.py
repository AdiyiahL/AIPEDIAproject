from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(verbose_name="name", max_length= 16 )
    pwd = models.CharField(verbose_name="password", max_length=64)
    mobile = models.CharField(verbose_name="mobile phone",max_length=64)
    email = models.CharField(verbose_name="email", max_length=32)
    age = models.IntegerField(verbose_name="age")
    subscribe = models.BooleanField(default=False)
    level = models.IntegerField(verbose_name="level",default=1)
    # gender = models.IntegerField(verbose_name="gender", choices=[(1,"male"),(2,"famale")])

class AdminUser(models.Model):
    name = models.CharField(verbose_name="name", max_length= 16 )
    pwd = models.CharField(verbose_name="password", max_length=64)
    mobile = models.CharField(verbose_name="mobile phone",max_length=64)
    email = models.CharField(verbose_name="email", max_length=32)