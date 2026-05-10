from django import forms

from .models import Stop, Activity


class StopForm(forms.ModelForm):

    class Meta:

        model = Stop

        fields = [
            'city',
            'start_date',
            'end_date',
            'order'
        ]


class ActivityForm(forms.ModelForm):

    class Meta:

        model = Activity

        fields = [
            'name',
            'time',
            'cost'
        ]