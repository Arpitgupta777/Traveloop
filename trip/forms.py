from django import forms
from .models import Trip, ItineraryStop, UserProfile,PackingItem, PlannedActivity, TripNote
from django.contrib.auth.models import User


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['name', 'description', 'start_date', 'end_date', 'is_public']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }



class StopForm(forms.ModelForm):
    class Meta:
        model = ItineraryStop
        # We don't include 'trip' because we will attach it automatically in the view
        fields = ['city_name', 'arrival_date', 'departure_date']
        widgets = {
            'arrival_date': forms.DateInput(attrs={'type': 'date'}),
            'departure_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ActivityForm(forms.ModelForm):
    class Meta:
        model = PlannedActivity
        # We don't include 'stop' because we will attach it automatically
        fields = ['activity_name', 'category', 'estimated_cost', 'scheduled_time']
        widgets = {
            'scheduled_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = TripNote
        fields = ['content']
        labels = {'content': ''} # Hides the label so it looks cleaner
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Save hotel codes, flight numbers, or quick reminders here...'}),
        }

class PackingItemForm(forms.ModelForm):
    class Meta:
        model = PackingItem
        fields = ['item_name']
        labels = {'item_name': ''}
        widgets = {
            'item_name': forms.TextInput(attrs={'placeholder': 'Add a packing item (e.g., Passport, Jacket)...'}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']
