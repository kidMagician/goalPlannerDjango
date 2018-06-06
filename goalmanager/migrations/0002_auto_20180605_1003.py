# Generated by Django 2.0.5 on 2018-06-05 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goalmanager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date',
            new_name='start_time',
        ),
        migrations.AddField(
            model_name='task',
            name='goal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goalmanager.Goal'),
        ),
    ]
