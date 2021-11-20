from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showtripsPageView(request) :
    return render(request, 'travelsites/showTrips.html')

def showAfricaPageView(request) :
    context = {
        "area" : "Africa"
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showAsiaPageView(request) :
    context = {
        "area" : "Asia"
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showAustraliaPageView(request) :
    context = {
        "area" : "Australia"
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showEuropePageView(request) :
    context = {
        "area" : "Europe"
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showNorthAmericaPageView(request) :
    context = {
        "area" : "North America"
    }
    return render(request, 'travelsites/displaytrips.html', context)

def showSouthAmericaPageView(request) :
    context = {
        "area" : "South America"
    }
    return render(request, 'travelsites/displaytrips.html', context)