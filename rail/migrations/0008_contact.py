# Generated by Django 4.0.2 on 2022-02-24 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rail', '0007_ticket_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msgid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('subject', models.CharField(default='', max_length=50)),
                ('text', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
