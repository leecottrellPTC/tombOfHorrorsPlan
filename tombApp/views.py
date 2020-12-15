from django.shortcuts import render
from django.http import HttpResponse
from tombApp.models import character
from tombApp.models import critter
from tombApp.models import battle

theChar = character()

# Create your views here.
def tobattle_page(request):  
    
    theCritter = critter('', 'Minotaur',76,14,17,6, 'static/images/minotaur.png')
    theBattle = battle()
    theBattle.charname = theChar.charname
    theBattle.charhp = theChar.hp
    theBattle.charac = theChar.ac 
    theBattle.critname = theCritter.name
    theBattle.crithp = theCritter.hp
    theBattle.critac = theCritter.ac 
    theBattle.critdam = theCritter.dam 
    theBattle.crithitbon = theCritter.hitbon
    theBattle.image_name = theCritter.image_name
    return render(request, 'tobattle.html', {'theBattle' : theBattle} )


def character_page(request):
    global theChar
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

