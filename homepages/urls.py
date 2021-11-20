from django.urls import path
from .views import indexPageView
from .views import aboutPageView

urlpatterns = [
    path("about/", aboutPageView, name="about"),
    path("", indexPageView, name="index"),
    
]