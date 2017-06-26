from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from login.models import*


def index(request):
    test="""<h1>Inception led welcomes you :)</h1>"""

    return HttpResponse(test)