#i have created this file
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse ("hello Faiz")


# def about(request):
#     return HttpResponse ("shadab about to die")


def index(request):
    return render(request,'index.html')




def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    print(djtext)
    print(removepunc)
    if removepunc == "on":

    # analyzed=djtext
       punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
       analyzed=""
       for char in djtext:
        if char not in punctuations:
            analyzed=analyzed+char
       b={'purpose':'Remove Punctuations','analyzed_Text':analyzed}


       return render(request,'analyze.html',b)
    elif(fullcaps=="on"):
       analyzed=""
       for char in djtext:
          analyzed=analyzed+char.upper()
          b={'purpose':'Changed to uppercase','analyzed_Text':analyzed}


       return render(request,'analyze.html',b)

    else:
       return HttpResponse("Error")


# def removepunc(request):
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalizefirst")