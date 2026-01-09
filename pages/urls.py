from django.urls import path
from .views import HomePageView
from .views import AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("home/", HomePageView.as_view(), name="homeTwo"),
    path("", AboutPageView.as_view(), name="about"),
    path("about/", AboutPageView.as_view(), name="aboutTwo")
]