# Generated by Django 2.1.3 on 2018-11-21 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileoutput',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='upload_fileoutput_runs', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='fileoutput',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='upload_fileoutput_runs', to='users.Project'),
        ),
    ]