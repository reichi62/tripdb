from django.shortcuts import render
from .models import Trip


# Create your views here.
def trip_overview(request):
    trips = Trip.objects.all()
    context = {'trips': trips}
    return render(request, 'trip_overview.html', context)


def welcome(request):
    return render(request, 'welcome.html')
