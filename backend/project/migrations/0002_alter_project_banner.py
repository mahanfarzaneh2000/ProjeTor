# Generated by Django 3.2.8 on 2021-11-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='banner',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='project_banner/'),
        ),
    ]
