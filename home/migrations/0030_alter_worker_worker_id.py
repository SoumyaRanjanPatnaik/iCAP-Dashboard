# Generated by Django 3.2.5 on 2021-08-09 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20210810_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='worker_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
