# Generated by Django 2.1.7 on 2019-03-16 20:12

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Charge",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stripe_id", models.CharField(max_length=255, unique=True)),
                ("amount", models.IntegerField()),
                ("amount_refunded", models.IntegerField()),
                ("balance_transaction", models.CharField(max_length=255)),
                ("captured", models.BooleanField(default=False)),
                ("created", models.DateTimeField()),
                (
                    "currency",
                    models.CharField(
                        choices=[("usd", "usd")], default="usd", max_length=3
                    ),
                ),
                ("dispute", models.BooleanField(default=False)),
                ("livemode", models.BooleanField(default=False)),
                ("paid", models.BooleanField(blank=True, null=True)),
                (
                    "receipt_email",
                    models.CharField(blank=True, default="", max_length=800),
                ),
                ("refunded", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("succeeded", "succeeded"),
                            ("pending", "pending"),
                            ("failed", "failed"),
                        ],
                        default="pending",
                        max_length=9,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stripe_id", models.CharField(max_length=255, unique=True)),
                ("livemode", models.BooleanField(default=False)),
                (
                    "account_balance",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=9, null=True
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        choices=[("usd", "usd")], default="usd", max_length=3
                    ),
                ),
                ("delinquent", models.BooleanField(default=False)),
                ("default_source", models.TextField(blank=True, null=True)),
                ("metadata", django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stripe_id", models.CharField(max_length=255, unique=True)),
                ("created", models.DateTimeField()),
                ("data", django.contrib.postgres.fields.jsonb.JSONField()),
                ("livemode", models.BooleanField(default=False)),
                ("request", models.CharField(max_length=255)),
                ("kind", models.CharField(max_length=64)),
                ("metadata", django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stripe_id", models.CharField(max_length=255, unique=True)),
                ("attempt_count", models.IntegerField()),
                ("attempted", models.BooleanField(default=False)),
                (
                    "currency",
                    models.CharField(
                        choices=[("usd", "usd")], default="usd", max_length=3
                    ),
                ),
                ("description", models.TextField(blank=True)),
                ("ending_balance", models.IntegerField(null=True)),
                ("forgiven", models.BooleanField(default=False)),
                (
                    "hosted_invoice_url",
                    models.CharField(blank=True, default="", max_length=799),
                ),
                (
                    "invoice_pdf",
                    models.CharField(blank=True, default="", max_length=799),
                ),
                ("livemode", models.BooleanField(default=False)),
                ("paid", models.BooleanField(default=False)),
                ("period_end", models.DateTimeField()),
                ("period_start", models.DateTimeField()),
                ("receipt_number", models.CharField(max_length=64, null=True)),
                ("starting_balance", models.IntegerField()),
                (
                    "statement_descriptor",
                    models.CharField(blank=True, default="", max_length=22),
                ),
                (
                    "subscription_proration_date",
                    models.DateTimeField(blank=True, null=True),
                ),
                ("subtotal", models.IntegerField(blank=True, null=True)),
                ("tax", models.IntegerField(blank=True, null=True)),
                (
                    "tax_percent",
                    models.DecimalField(decimal_places=2, max_digits=5, null=True),
                ),
                ("total", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Plan",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stripe_id", models.CharField(max_length=255, unique=True)),
                ("active", models.BooleanField(default=False)),
                (
                    "aggregate_usage",
                    models.CharField(
                        choices=[
                            ("sum", "sum"),
                            ("last_during_period", "last_during_period"),
                            ("max", "max"),
                            ("last_ever", "LAST_EVER"),
                        ],
                        default="sum",
                        max_length=18,
                        null=True,
                    ),
                ),
                ("amount", models.IntegerField()),
                ("created", models.DateTimeField(blank=True, null=True)),
                (
                    "currency",
                    models.CharField(
                        choices=[("usd", "usd")], default="usd", max_length=3
                    ),
                ),
                (
                    "interval",
                    models.CharField(
                        choices=[
                            ("day", "day"),
                            ("week", "week"),
                            ("month", "month"),
                            ("year", "year"),
                        ],
                        default="month",
                        max_length=5,
                    ),
                ),
                ("livemode", models.BooleanField(default=False)),
                ("metadata", django.contrib.postgres.fields.jsonb.JSONField()),
                ("nickname", models.CharField(max_length=255)),
                ("trial_period_days", models.IntegerField(default=0, null=True)),
                (
                    "usage_type",
                    models.CharField(
                        choices=[("licensed", "licensed"), ("metered", "metered")],
                        max_length=8,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stripe_id", models.CharField(max_length=255, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("metadata", django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stripe_id", models.CharField(max_length=255, unique=True)),
                ("livemode", models.BooleanField(default=False)),
                ("metadata", django.contrib.postgres.fields.jsonb.JSONField()),
                ("cancel_at_period_end", models.BooleanField(default=False, null=True)),
                ("current_period_start", models.DateTimeField(blank=True, null=True)),
                ("current_period_end", models.DateTimeField(blank=True, null=True)),
                ("canceled_at", models.DateTimeField(blank=True, null=True)),
                ("ended_at", models.DateTimeField(blank=True, null=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscriptions",
                        to="billing.Customer",
                    ),
                ),
                (
                    "plans",
                    models.ManyToManyField(
                        related_name="subscriptions", to="billing.Plan"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubscriptionItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stripe_id", models.CharField(max_length=255, unique=True)),
                ("livemode", models.BooleanField(default=False)),
                ("created", models.DateTimeField()),
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="subscription_items",
                        to="billing.Plan",
                    ),
                ),
                (
                    "subscription",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscription_items",
                        to="billing.Subscription",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UsageRecord",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stripe_id", models.CharField(max_length=255, unique=True)),
                ("livemode", models.BooleanField(default=False)),
                (
                    "action",
                    models.CharField(
                        choices=[("increment", "increment"), ("set", "set")],
                        default="increment",
                        max_length=9,
                    ),
                ),
                ("quantity", models.IntegerField(default=0)),
                ("timestamp", models.DateTimeField()),
                (
                    "subscription_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="usage_records",
                        to="billing.SubscriptionItem",
                    ),
                ),
            ],
        ),
    ]
