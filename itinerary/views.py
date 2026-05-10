from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import (
    Trip,
    Stop,
    Activity
)

from .forms import (
    StopForm,
    ActivityForm
)


def itinerary_builder(request, trip_id):

    trip = get_object_or_404(
        Trip,
        id=trip_id
    )

    if request.method == 'POST':

        stop_form = StopForm(request.POST)

        if stop_form.is_valid():

            stop = stop_form.save(commit=False)

            stop.trip = trip

            stop.save()

            return redirect(
                'trip_detail',
                trip_id=trip.id
            )

    else:
        stop_form = StopForm()

    stops = Stop.objects.filter(
        trip=trip
    ).order_by('order')

    context = {
        'trip': trip,
        'stops': stops,
        'stop_form': stop_form
    }

    return render(
        request,
        'itinerary/builder.html',
        context
    )


def add_activity(request, stop_id):

    stop = get_object_or_404(
        Stop,
        id=stop_id
    )

    if request.method == 'POST':

        form = ActivityForm(request.POST)

        if form.is_valid():

            activity = form.save(commit=False)

            activity.stop = stop

            activity.save()

            return redirect(
                'trip_detail',
                trip_id=stop.trip.id
            )

    else:
        form = ActivityForm()

    return render(
        request,
        'itinerary/add_activity.html',
        {
            'form': form,
            'stop': stop
        }
    )


def trip_detail(request, trip_id):

    trip = get_object_or_404(
        Trip,
        id=trip_id
    )

    stops = Stop.objects.filter(
        trip=trip
    ).order_by('order')

    return render(
        request,
        'itinerary/trip_detail.html',
        {
            'trip': trip,
            'stops': stops
        }
    )