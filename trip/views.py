from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum

from .models import Trip, ItineraryStop, PlannedActivity, PackingItem
from .forms import PackingItemForm, TripForm, StopForm, ActivityForm, NoteForm, TripForm 

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views

from .models import UserProfile
from .forms import UserUpdateForm, ProfileUpdateForm


@login_required
def dashboard(request):
    today = timezone.now().date()
    
    # ONGOING: Started today or earlier AND ends today or later
    ongoing_trips = Trip.objects.filter(user=request.user, start_date__lte=today, end_date__gte=today).order_by('end_date')
    
    # FUTURE: Starts after today
    future_trips = Trip.objects.filter(user=request.user, start_date__gt=today).order_by('start_date')
    
    # COMPLETED: Ended before today
    completed_trips = Trip.objects.filter(user=request.user, end_date__lt=today).order_by('-end_date')

    context = {
        'ongoing_trips': ongoing_trips,
        'future_trips': future_trips,
        'completed_trips': completed_trips,
    }
    return render(request, 'trip/dashboard.html', context)


@login_required
def create_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            # commit=False tells Django: "Wait! Don't save to the database yet!"
            trip = form.save(commit=False) 
            
            # Now we securely attach the logged-in user to this trip
            trip.user = request.user 
            
            # NOW we save it!
            trip.save() 
            
            # Send them back to the dashboard to see their new trip
            return redirect('dashboard') 
    else:
        # If they just loaded the page, show them an empty form
        form = TripForm()

    return render(request, 'trip/create_trip.html', {'form': form})

@login_required
def trip_detail(request, trip_id):
    # Securely fetch the specific trip ONLY if it belongs to the logged-in user
    trip = get_object_or_404(Trip, id=trip_id, user=request.user)
    return render(request, 'trip/trip_detail.html', {'trip': trip})

@login_required
def add_stop(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, user=request.user)
    
    if request.method == 'POST':
        trip = get_object_or_404(Trip, id=trip_id, user=request.user)
        form = StopForm(request.POST)
        if form.is_valid():
            stop = form.save(commit=False)
            stop.trip = trip
            stop.save()
    return redirect('trip_detail', trip_id=trip_id)

@login_required
def add_activity(request, stop_id):
    stop = get_object_or_404(ItineraryStop, id=stop_id, trip__user=request.user)
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.stop = stop
            activity.save()
    return redirect('trip_detail', trip_id=stop.trip.id)


@login_required
def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, user=request.user)

    # 1. Budget Math
    activities = PlannedActivity.objects.filter(stop__trip=trip)
    total_budget = activities.aggregate(Sum('estimated_cost'))['estimated_cost__sum'] or 0.00
    category_costs = activities.values('category').annotate(total=Sum('estimated_cost')).order_by('-total')

    # 2. Forms Logic (Notes and Packing)
    if request.method == 'POST':
        if 'content' in request.POST:
            note_form = NoteForm(request.POST)
            if note_form.is_valid():
                note = note_form.save(commit=False)
                note.trip = trip
                note.save()
                return redirect('trip_detail', trip_id=trip.id)
        elif 'item_name' in request.POST:
            packing_form = PackingItemForm(request.POST)
            if packing_form.is_valid():
                item = packing_form.save(commit=False)
                item.trip = trip
                item.save()
                return redirect('trip_detail', trip_id=trip.id)

    # 3. Pass ALL forms to the template so we don't need a separate page
    context = {
        'trip': trip,
        'total_budget': total_budget,
        'category_costs': category_costs,
        'note_form': NoteForm(),
        'packing_form': PackingItemForm(),
        'stop_form': StopForm(),         # <-- ADDED THIS
        'activity_form': ActivityForm(), # <-- ADDED THIS
    }
    return render(request, 'trip/trip_detail.html', context)

@login_required
def toggle_packing_item(request, item_id):
    # Securely fetch the item, ensuring it belongs to the logged-in user
    item = get_object_or_404(PackingItem, id=item_id, trip__user=request.user)
    
    # Flip the boolean switch! If it's True, make it False. If False, make it True.
    item.is_packed = not item.is_packed 
    item.save()
    
    # Send them right back to the trip page
    return redirect('trip_detail', trip_id=item.trip.id)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Automatically log them in after signing up
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    
    return render(request, 'trip/register.html', {'form': form})

def home(request):
    # Fetch the 6 newest public trips
    recent_public_trips = Trip.objects.filter(is_public=True).order_by('-created_at')[:6]
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    return render(request, 'trip/index.html', {'public_trips': recent_public_trips})

@login_required
def profile(request):
    # Ensure a profile exists for this user
    UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # request.FILES is required for image uploads!
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'trip/profile.html', context)

def community(request):
    # Fetch ALL public trips
    public_trips = Trip.objects.filter(is_public=True).order_by('-created_at')
    return render(request, 'trip/community.html', {'trips': public_trips})

def public_trip_detail(request, trip_id):
    # Fetch the trip ONLY if it is marked as public
    trip = get_object_or_404(Trip, id=trip_id, is_public=True)
    
    # Calculate the total budget just for viewing
    activities = PlannedActivity.objects.filter(stop__trip=trip)
    total_budget = activities.aggregate(Sum('estimated_cost'))['estimated_cost__sum'] or 0.00
    category_costs = activities.values('category').annotate(total=Sum('estimated_cost')).order_by('-total')

    context = {
        'trip': trip,
        'total_budget': total_budget,
        'category_costs': category_costs,
    }
    return render(request, 'trip/public_trip_detail.html', context)
