from django.shortcuts import render
from django.http import HttpResponse

class character:
  def __init__(self, name, hp, ac):
    self.charname = name
    self.hp = hp
    self.ac = ac

theChar = character("", "", "")

# Create your views here.

def character_page(request):
    if request.method == 'POST':
        theChar = character(request.POST.get("charname"),
        request.POST.get("hitpoints"),
        request.POST.get("armor"))
        return render(request, 'player.html', {'theChar' : theChar})
    else:
        return render(request, 'character.html')

def home_page(request):
    return render(request, 'home.html')

def lore_page(request):
    return render(request, 'lore.html')

