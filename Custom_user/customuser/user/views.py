from django.shortcuts import render # type: ignore
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello, World!")

# Create your views here.
