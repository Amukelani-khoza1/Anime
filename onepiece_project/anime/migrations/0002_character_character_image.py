# Generated by Django 5.1.3 on 2024-12-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='character_image',
            field=models.ImageField(default=None, upload_to='character_images/'),
        ),
    ]