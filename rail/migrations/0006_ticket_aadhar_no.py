# Generated by Django 4.0.2 on 2022-02-24 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rail', '0005_ticket_age_ticket_destination_ticket_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='aadhar_no',
            field=models.IntegerField(default=0),
        ),
    ]
