# Generated by Django 4.1.5 on 2023-03-09 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/batman.png', upload_to=''),
        ),
    ]
