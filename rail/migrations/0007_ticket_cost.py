# Generated by Django 4.0.2 on 2022-02-24 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rail', '0006_ticket_aadhar_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='cost',
            field=models.IntegerField(default=0),
        ),
    ]
