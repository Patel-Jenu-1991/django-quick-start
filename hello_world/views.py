# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<html><body>Hello, World!</body></html>')

def about(request):
    msg = "Here is the About Page. Want to return home? \
    <a href='/'>Back Home</a>"
    return HttpResponse(msg)
