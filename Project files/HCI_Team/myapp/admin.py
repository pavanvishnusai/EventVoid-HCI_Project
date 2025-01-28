from django.contrib import admin
from .models import Events_List, Participant

class EventsListAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'location', 'event_date', 'rules', 'rating')

admin.site.register(Events_List, EventsListAdmin)

class BookingAdmin(admin.ModelAdmin):
    fields = ('event', 'name','email','phone')

admin.site.register(Participant, BookingAdmin)


# Register your models here.
