# Generated by Django 5.1.3 on 2024-12-09 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_gallery_title_alter_gallery_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='images')),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
    ]
