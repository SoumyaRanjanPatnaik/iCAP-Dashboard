# Generated by Django 3.2.5 on 2021-08-09 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_log_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'ordering': ['-datetime']},
        ),
        migrations.AlterField(
            model_name='worker',
            name='worker_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
