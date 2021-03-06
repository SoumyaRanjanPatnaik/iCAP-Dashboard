# Generated by Django 3.2.5 on 2021-08-05 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20210722_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worker',
            old_name='location',
            new_name='location_of_work',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='avg_bpm',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='curr_bpm',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='fall',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='height',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='id',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='temperature',
        ),
        migrations.AddField(
            model_name='worker',
            name='worker_id',
            field=models.AutoField(default=-1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField(max_length=50)),
                ('avg_bpm', models.FloatField(max_length=50)),
                ('curr_bpm', models.FloatField(max_length=50)),
                ('temperature', models.FloatField(max_length=50)),
                ('fall', models.BooleanField(default=False)),
                ('worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.worker')),
            ],
        ),
    ]
