from django.db import models

# Create your models here.
import users.models


class ContentLevel(models.Model):
    title = models.CharField(verbose_name="title", max_length=32)
    level = models.IntegerField(verbose_name="level")

class NewContent(models.Model):
    title = models.CharField(verbose_name="title", max_length=1000)
    what_area = models.CharField(verbose_name="what_area",max_length=3000)
    how_area = models.CharField(verbose_name="how_area", max_length=3000)
    example = models.CharField(verbose_name="example_area", max_length=3000,null=True,blank=True)
    source = models.CharField(verbose_name="source_area", max_length=2000,null=True,blank=True)
    try_area = models.CharField(verbose_name="try_area", max_length=3000)
    userId = models.ForeignKey(verbose_name="author", to=users.models.UserInfo,on_delete=models.CASCADE)
