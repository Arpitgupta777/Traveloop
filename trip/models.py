from django.db import models
from django.contrib.auth.models import User

# 1. The Master Folder for a Vacation
class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Links trip to the logged-in user
    name = models.CharField(max_length=200) # e.g., "Euro Trip 2024"
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_public = models.BooleanField(default=False) # For the community tab later
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"

# 2. The Cities / Destinations visited during the Trip
class ItineraryStop(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='stops')
    city_name = models.CharField(max_length=150) # The user just types "Paris"
    arrival_date = models.DateField()
    departure_date = models.DateField()

    def __str__(self):
        return f"{self.city_name} on {self.trip.name}"

# 3. The Things to Do & Budgeting
class PlannedActivity(models.Model):
    # Django Choices for our simple dropdown menu
    CATEGORY_CHOICES = [
        ('Stay', 'Accommodation'),
        ('Transport', 'Transportation'),
        ('Food', 'Food & Dining'),
        ('Sightseeing', 'Sightseeing & Tours'),
        ('Other', 'Other'),
    ]

    stop = models.ForeignKey(ItineraryStop, on_delete=models.CASCADE, related_name='activities')
    activity_name = models.CharField(max_length=200) # e.g., "Eiffel Tower"
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Sightseeing')
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # For our budget math!
    scheduled_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.activity_name} ({self.stop.city_name})"

# 4. The Packing List Checklist
class PackingItem(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='packing_items')
    item_name = models.CharField(max_length=150) # e.g., "Passport"
    is_packed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item_name} for {self.trip.name}"

# 5. The Digital Scratchpad
class TripNote(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField() # e.g., "Hotel confirmation code: X78B9"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.trip.name}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
