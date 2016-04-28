import requests
from django.shortcuts import render
from django.http import HttpResponse
import urllib2, httplib

from .models import Greeting

# Create your views here.
def index(request):
    r = "Hello World"
    print r
    return HttpResponse(r)