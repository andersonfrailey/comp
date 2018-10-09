# Generated by Django 2.1 on 2018-10-09 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('taxcalc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxcalcoutput',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='taxcalc_taxcalcoutput_runs', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='taxcalcoutput',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='taxcalc_taxcalcoutput_runs', to='users.Project'),
        ),
    ]
