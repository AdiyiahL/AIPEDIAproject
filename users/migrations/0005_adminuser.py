# Generated by Django 4.2.4 on 2023-08-09 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20230615_0058'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='name')),
                ('pwd', models.CharField(max_length=64, verbose_name='password')),
                ('mobile', models.CharField(max_length=64, verbose_name='mobile phone')),
                ('email', models.CharField(max_length=32, verbose_name='email')),
            ],
        ),
    ]
