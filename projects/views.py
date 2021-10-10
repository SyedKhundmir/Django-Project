from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request,'projects/homepage.html')

def about(request):
    return render(request,'projects/about.html')

def contact(request):
    return render(request,'projects/contact.html')
