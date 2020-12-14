from django.shortcuts import render
from django.http import HttpResponse
from tombApp.models import character


# Create your views here.

def character_page(request):
    theChar = character()
    if request.method == 'POST':
        theChar = character('',request.POST.get('charname'),
        request.POST.get('hitpoints'),
        request.POST.get('armor'))
        
        return render(request, 'player.html', {'theChar' : theChar})
    else:
        return render(request, 'character.html', {'theChar' : theChar})
       

def home_page(request):
    return render(request, 'home.html')

def lore_page(request):
    return render(request, 'lore.html')

if __name__ == '__main__':
    #if calls the class if it is not instantiated elsewhere
    theChar = character("","","")

