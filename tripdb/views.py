from django.shortcuts import render, get_object_or_404
from .models import Trip, Day


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def trip_overview(request):
    trips = Trip.objects.all()
    context = {'trips': trips}
    return render(request, 'trip_overview.html', context)


def trip_details(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    days = Day.objects.filter(trip_id=trip.id)
    context = {"trip": trip, "days": days}
    return render(request, 'trip_details.html', context)
