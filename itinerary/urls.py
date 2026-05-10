from django.urls import path

from . import views


urlpatterns = [

    path(
        'builder/<int:trip_id>/',
        views.itinerary_builder,
        name='builder'
    ),

    path(
        'trip/<int:trip_id>/',
        views.trip_detail,
        name='trip_detail'
    ),

    path(
        'activity/<int:stop_id>/',
        views.add_activity,
        name='add_activity'
    ),
]