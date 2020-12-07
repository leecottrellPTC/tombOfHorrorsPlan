from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def lore_page(request):
    return render(request, 'lore.html')

def character_page(request):
    return render(request, 'character.html')