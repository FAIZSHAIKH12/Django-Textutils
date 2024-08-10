from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("hello faiz")

# Create your views here.
