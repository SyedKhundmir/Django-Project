from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path
from django.urls.conf import include

import projects

def home(request):
    return HttpResponse("Home dude!!!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('projects.urls')),
]
