# Generated by Django 4.2.10 on 2024-02-20 18:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_payment_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='bagages',
        ),
        migrations.RemoveField(
            model_name='car',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='car',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='car',
            name='seats',
        ),
        migrations.CreateModel(
            name='Validation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('upated_at', models.DateTimeField(auto_now=True)),
                ('bagages', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.bagages')),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.car')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.customeruser')),
                ('reservation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.reservation')),
                ('seats', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.seats')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='bagages',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.bagages'),
        ),
        migrations.AddField(
            model_name='car',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.customeruser'),
        ),
        migrations.AddField(
            model_name='car',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.driver'),
        ),
        migrations.AddField(
            model_name='car',
            name='seats',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.seats'),
        ),
    ]
