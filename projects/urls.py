from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.homepage, name="homepg"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
]