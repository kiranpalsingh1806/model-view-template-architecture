from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import Contact

# Create your views here.


def index(request):
    context = {
        "variable": "Kiranpal Singh"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is Home Page")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is About Page")


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is Services Page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()

    return render(request, 'contact.html')
