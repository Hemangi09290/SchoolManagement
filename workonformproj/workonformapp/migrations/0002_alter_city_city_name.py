# Generated by Django 3.2.5 on 2022-05-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workonformapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(default='New Delhi', max_length=100),
        ),
    ]