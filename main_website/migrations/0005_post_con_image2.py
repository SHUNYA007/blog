# Generated by Django 2.2.6 on 2019-12-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_website', '0004_auto_20191206_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='con_image2',
            field=models.ImageField(default='panda.jpg', upload_to='content_img'),
        ),
    ]
