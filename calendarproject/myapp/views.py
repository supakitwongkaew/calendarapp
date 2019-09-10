from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

def index(req):
    entries = Entry.objects.all()
    return render(req, 'myapp/myapp.html', { 'entries': entries }) 

def myapp(req):
    return render(req, 'myapp/index.html')

def whatthefantastic(req):
    return HttpResponse('3000')

def dosomething(req):
    return HttpResponse('I do nothing')
