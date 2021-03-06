# Generated by Django 2.1.7 on 2019-03-16 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("billing", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="project",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.Project",
            ),
        ),
        migrations.AddField(
            model_name="plan",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="plans",
                to="billing.Product",
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="charge",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="latest_invoice",
                to="billing.Charge",
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="invoices",
                to="billing.Customer",
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="subscription",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="invoices",
                to="billing.Subscription",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="charge",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="charge",
                to="billing.Charge",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customer",
                to="billing.Customer",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="invoice",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="invoice",
                to="billing.Invoice",
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="charge",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="charges",
                to="billing.Customer",
            ),
        ),
    ]
