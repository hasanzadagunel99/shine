from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(requests):
    context={
        "name": "Django"
    }
    return render(requests, "index.html", context = context )


def shop(requests):
    return render (requests, 'shop.html')
