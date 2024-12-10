# Generated by Django 5.1.3 on 2024-12-04 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.TextField(default='biriyani', max_length=100),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
