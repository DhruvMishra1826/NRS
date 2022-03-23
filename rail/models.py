from django.db import models

# Create your models here.
class Train(models.Model):
    id = models.AutoField(primary_key=True)
    train_name = models.CharField(max_length=50, default="")
    source = models.CharField(max_length=50, default="")
    destination = models.CharField(max_length=50, default="")
    seats_available = models.IntegerField(default=0)
    fare_in_rupees = models.IntegerField(default=0)
    depart_time = models.TimeField(blank=True, null=True)
    arrival_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.train_name

class Passenger(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=50, default="")
    aadhar_no = models.IntegerField(default=0)
    source = models.CharField(max_length=50, default="")
    destination = models.CharField(max_length=50, default="")
    train_name = models.CharField(max_length=50, default="")
    date_of_journey = models.DateField(blank=True, null=True)
    phone_no = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=50, default="")
    aadhar_no = models.IntegerField(default=0)
    train_name = models.CharField(max_length=50, default="")
    date_of_journey = models.DateField(blank=True, null=True)
    source = models.CharField(max_length=50, default="")
    destination = models.CharField(max_length=50, default="")
    reservation_status = models.CharField(max_length=50, default="Not Confirm")
    seat_number = models.IntegerField(default=0)
    pnr_no = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    msgid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,default="")
    subject = models.CharField(max_length=50,default="")
    text = models.CharField(max_length=500,default="")


    def __str__(self):
        return self.name