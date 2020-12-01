from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    html = "<html><body><h1>Welcome to the Tomb of Horrors</h1></html></body>"
    return HttpResponse(html)
