from django.urls import path
from .views import showtripsPageView
from .views import showAfricaPageView
from .views import showAsiaPageView
from .views import showAustraliaPageView
from .views import showEuropePageView
from .views import showNorthAmericaPageView
from .views import showSouthAmericaPageView

urlpatterns = [
    path("", showtripsPageView, name="showtrips"),
    path("africa/", showAfricaPageView, name="realestate"), #maybe will need to change the name africa
    path("asia/", showAsiaPageView, name="auto"), #asia
    path("australia/", showAustraliaPageView, name="antique"), #australia
    path("europe/", showEuropePageView, name="bankaccount"), #europe
    path("northamerica/", showNorthAmericaPageView, name="stocks/bonds"), #northamerica
    path("southamerica/", showSouthAmericaPageView, name="donate"), #southamerica
]