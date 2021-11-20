from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
from .models import TripCategory



# Create your views here.
def showtripsPageView(request) :
    return render(request, 'travelsites/showTrips.html')

def showAfricaPageView(request) :
    id = TripCategory.objects.get(description = "Africa") # change to Real Estate
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description, #change id description to Real Estate in the database
        "image" : data.main_photo 
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showAsiaPageView(request) :
    id = TripCategory.objects.get(description = "Asia") # change to Auto
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "image" : data.main_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showAustraliaPageView(request) :
    id = TripCategory.objects.get(description = "Australia") # change to Bank Account
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "image" : data.main_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showEuropePageView(request) :
    id = TripCategory.objects.get(description = "Europe") # change to Stocks/Bonds
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "image" : data.main_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showNorthAmericaPageView(request) :
    id = TripCategory.objects.get(description = "North America") # change to Antique!
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "image" : data.main_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showSouthAmericaPageView(request) :
    id = TripCategory.objects.get(description = "South America") # change to Donate!
    data = Destination.objects.get(trip_category_id = id)
    context = {
        "area" : id.description,
        "image" : data.main_photo
    }
    return render(request, 'travelsites/displaytrips.html', context)