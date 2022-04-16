from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "variable": "Kiranpal Singh"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is Home Page")


def about(request):
    return HttpResponse("This is About Page")


def services(request):
    return HttpResponse("This is Services Page")


def contact(request):
    return HttpResponse("This is Contact Page")
