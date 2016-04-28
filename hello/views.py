import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import urllib2, httplib

from .models import Greeting

pid = 0

# Create your views here.
def index(request):
    r = "Hello World!"
    print r
    return HttpResponse(r)
    
    
def gif(request):
    return HttpResponseRedirect('https://i.imgur.com/pXjrQ.gif')
    
def robots(request):
    content = 'fillertext'
    response = HttpResponse(content, content_type='text/plain; charset=utf-8')
    return response
    
    
def posts(request):
    return HttpResponse("Posts Page!")
    
    
def postsnew(request):
    if request.method == 'POST':
        #submit form
        return HttpResponse('posted to postsnew')
    else:
        #GET request
        return render(request, 'postsnew.html')