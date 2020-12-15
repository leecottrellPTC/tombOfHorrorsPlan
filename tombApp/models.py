from django.db import models

# Create your models here.


class character(models.Model):
    charname = models.CharField(max_length=40, default="", help_text="Your name")
    hp = models.IntegerField(default=1, help_text="Hit Points")
    ac = models.IntegerField(default=10, help_text="Armor Class")

class critter(models.Model):
    name = models.CharField(max_length=40, default="", help_text="Critter name")
    hp = models.IntegerField(default=1, help_text="Hit Points")
    ac = models.IntegerField(default=10, help_text="Armor Class")
    dam = models.IntegerField(default=5, help_text="Damage Done")
    hitbon = models.IntegerField(default=6, help_text="Damage Done")
    image_name = models.CharField(max_length=100,default="static/images/tombmouth.jpg", help_text="Critter Image")
    
class battle(models.Model):
    charname = models.CharField(max_length=40, default="", help_text="Char name")
    charhp = models.IntegerField(default=1, help_text="Char Hit Points")
    charac = models.IntegerField(default=10, help_text="Char Armor Class")
    critname = models.CharField(max_length=40, default="", help_text="Critter name")
    crithp = models.IntegerField(default=1, help_text="Hit Points")
    critac = models.IntegerField(default=10, help_text="Armor Class")
    critdam = models.IntegerField(default=5, help_text="Damage Done")
    crithitbon = models.IntegerField(default=6, help_text="Damage Done")
    image_name = models.CharField(max_length=100,default="static/images/tombmouth.jpg", help_text="Critter Image")


