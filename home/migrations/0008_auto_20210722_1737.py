# Generated by Django 3.1.8 on 2021-07-22 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210722_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]