# Generated by Django 4.0.2 on 2022-02-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rail', '0003_passenger_train_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('train_name', models.CharField(default='', max_length=50)),
                ('date_of_journey', models.DateField(blank=True, null=True)),
                ('reservation_status', models.CharField(default='Not Confirm', max_length=50)),
                ('seat_number', models.IntegerField(default=0)),
                ('pnr_no', models.IntegerField(default=0)),
            ],
        ),
    ]
