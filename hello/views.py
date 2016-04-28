import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import urllib2, httplib

from .models import Greeting

# Create your views here.
def index(request):
    r = "Hello World!"
    print r
    return HttpResponse(r)
    
    
def gif(request):
    return HttpResponseRedirect('https://i.imgur.com/pXjrQ.gif')