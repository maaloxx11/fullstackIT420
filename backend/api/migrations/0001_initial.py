# Generated by Django 3.1.2 on 2020-11-22 09:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('price_id', models.CharField(default=0, max_length=20, primary_key=True, serialize=False)),
                ('price_description', models.CharField(max_length=30)),
                ('price_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('renter_id', models.IntegerField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=300)),
                ('telephone', models.IntegerField()),
                ('date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.IntegerField(primary_key=True, serialize=False)),
                ('room_type', models.IntegerField()),
                ('electric_meter_old', models.IntegerField(blank=True, null=True)),
                ('water_meter_old', models.IntegerField(blank=True, null=True)),
                ('electric_meter_new', models.IntegerField(default=0)),
                ('water_meter_new', models.IntegerField(default=0)),
                ('room_status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Transition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('move_in_date', models.DateField()),
                ('move_out_date', models.DateField(blank=True, null=True)),
                ('renter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.renter')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.room')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateField(blank=True, default=datetime.date.today)),
                ('deadline_date', models.DateField(blank=True, null=True)),
                ('total', models.FloatField(default=0)),
                ('price_electric_meter', models.IntegerField(blank=True, null=True)),
                ('price_water_meter', models.IntegerField(blank=True, null=True)),
                ('payment_status', models.IntegerField(default=1)),
                ('status', models.IntegerField(default=1)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.room')),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promblem_description', models.TextField(max_length=100)),
                ('problem_date', models.DateField()),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.room')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_payment', models.FloatField()),
                ('payment_date', models.DateField()),
                ('sc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.servicecharge')),
            ],
        ),
    ]
