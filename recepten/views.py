from django.shortcuts import render
import pymongo
from pymongo import MongoClient

# Create your views here.

client = MongoClient()

db = client.receptDB
recepten = db.recepten

def voegToe(request):
    alle_recepten = []
    if request.method == 'POST':
        naam = request.POST.get('naam')
        cal = request.POST.get('cal')
        ingr = request.POST.get('ingr')
        tijd = request.POST.get('tijd')

        if not recepten.find_one({"naam": naam}):
            recept = {
            "naam": naam,
            "cal": int(cal),
            "ingred": ingr,
            "tijd": tijd
            }
            recepten.insert_one(recept)
            alle_recepten = recepten.find()
            return render(request, 'recepten/index.html', {'alle_recepten': alle_recepten} )
        else:
            return render(request, 'recepten/bestaatreeds.html', None)
    else:
        alle_recepten = recepten.find()
        return render(request, 'recepten/index.html', {'alle_recepten': alle_recepten} )

def sortbycalorie(request):
    alle_recepten = []
    alle_recepten =  recepten.find().sort("cal", 1)
    return render(request, 'recepten/index.html', {'alle_recepten': alle_recepten})

def sortbynaam(request):
    alle_recepten = []
    alle_recepten = recepten.find().sort("naam", 1)
    return render(request, 'recepten/index.html', {'alle_recepten': alle_recepten})
