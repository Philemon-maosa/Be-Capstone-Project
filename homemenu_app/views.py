from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to HomeMenu App Backend</h1><p>API is running successfully.</p>")
