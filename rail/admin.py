from django.contrib import admin

# Register your models here.
from .models import Train, Passenger, Ticket, Contact

admin.site.register(Train)
admin.site.register(Passenger)
admin.site.register(Ticket)
admin.site.register(Contact)