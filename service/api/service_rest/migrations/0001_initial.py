# Generated by Django 4.0.3 on 2022-08-04 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutomobileVO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_href', models.CharField(max_length=200, unique=True)),
                ('color', models.CharField(max_length=50)),
                ('year', models.PositiveSmallIntegerField()),
                ('vin', models.CharField(max_length=17, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('employee_number', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=17)),
                ('reason', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('is_VIP', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service_appointment', to='service_rest.customer')),
                ('technician', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='service_appointment', to='service_rest.technician')),
            ],
        ),
    ]
