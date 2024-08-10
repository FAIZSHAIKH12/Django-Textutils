
from django.shortcuts import render,HttpResponse

# Create your views here.

def fun(request):
    return HttpResponse("hello faiz")


def home(request):
    return render(request,"index.html")
