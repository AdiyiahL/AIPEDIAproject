# Generated by Django 4.2.4 on 2023-08-08 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_level_lable_newcourses'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcontent',
            name='image_data',
            field=models.ImageField(default='user_image.jpg', upload_to='user_images'),
        ),
        migrations.AddField(
            model_name='newcontent',
            name='image_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
