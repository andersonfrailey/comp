# Generated by Django 2.1.2 on 2018-10-12 18:07

import datetime
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import re
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_gui_field_inputs', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True)),
                ('gui_field_inputs', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True)),
                ('inputs_file', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('errors_warnings_text', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True)),
                ('upstream_parameters', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('first_year', models.IntegerField(default=None, null=True)),
                ('years_n', models.CharField(max_length=300, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FileOutput',
            fields=[
                ('outputs', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True)),
                ('aggr_outputs', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True)),
                ('error_text', models.CharField(blank=True, default=None, max_length=4000, null=True)),
                ('run_time', models.IntegerField(default=0)),
                ('run_cost', models.DecimalField(decimal_places=4, default=0.0, max_digits=9)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, tzinfo=utc))),
                ('exp_comp_datetime', models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, tzinfo=utc))),
                ('job_id', models.UUIDField(blank=True, default=None, null=True)),
                ('upstream_vers', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('webapp_vers', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('inputs', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='outputs', to='upload.FileInput')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
