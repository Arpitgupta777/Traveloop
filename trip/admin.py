from django.contrib import admin
from .models import Trip, ItineraryStop, PlannedActivity, PackingItem, TripNote

# This tells Django to show these tables in the Admin Dashboard
admin.site.register(Trip)
admin.site.register(ItineraryStop)
admin.site.register(PlannedActivity)
admin.site.register(PackingItem)
admin.site.register(TripNote)