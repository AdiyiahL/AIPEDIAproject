from django.db import models

# Create your models here.

class ContentLevel(models.Model):
    title = models.CharField(verbose_name="title", max_length=32)
    level = models.IntegerField(verbose_name="level")
