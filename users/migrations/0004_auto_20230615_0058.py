# Generated by Django 3.0 on 2023-06-14 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230615_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='mobile',
            field=models.CharField(max_length=64, verbose_name='mobile phone'),
        ),
    ]
