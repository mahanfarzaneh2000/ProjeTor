# Generated by Django 3.2.8 on 2021-11-28 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='company_logo/'),
        ),
    ]
