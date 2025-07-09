from django.shortcuts import render
from .models import *
from .forms import SupportQuestionsForm


def index(request):
    info = infomain.objects.first()
    return render(request, "index.html", {"info": info})

def bonus(request):
    return render(request, "bonus.html")

def cleaning(request):
    cleaning_appliances = CleaningAppliance.objects.all()
    return render(request, "cleaning.html", {"cleaning_appliances": cleaning_appliances})

def instructions(request):
    cooking_appliances = CookingAppliance.objects.all()
    cleaning_appliances = CleaningAppliance.objects.all()
    return render(request, "instructions.html", {"cooking_appliances": cooking_appliances, "cleaning_appliances": cleaning_appliances})

def kitchen(request):
    cooking_appliances = CookingAppliance.objects.all()
    return render(request, "kitchen.html", {"cooking_appliances": cooking_appliances})

def productCleaning(request, pk):
    cleaning_appliances = CleaningAppliance.objects.get(pk=pk)
    return render(request, "productCleaning.html", {"cleaning_appliances": cleaning_appliances})

def productCooking(request, pk):
    cooking_appliance = CookingAppliance.objects.get(pk=pk)
    return render(request, "productCooking.html", {"cooking_appliance": cooking_appliance})

def recipes(request):
    recipes = Recipes.objects.all()
    return render(request, "recipes.html", {"recipes": recipes})

def support(request):
    support = Support.objects.first()
    Supportfaq = SupportFAQ.objects.all()
    form = SupportQuestionsForm(request.POST or None)
    success = False
    if request.method == 'POST' and form.is_valid():
        form.save()
        success = True
        form = SupportQuestionsForm()  # сброс формы
    return render(request, "support.html", {"support": support, "Supportfaq": Supportfaq, "form": form, "success": success})