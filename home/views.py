from django.shortcuts import render, redirect
from .models import Cities

def index(request):

    citis = Cities.objects.all()

    return render(request, "index.html", {'citis' : citis})

def addcity(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        img = request.FILES['img']
        cities = Cities(title = title, desc = desc, img = img)
        cities.save()
        return redirect("homepage")
    else:
        return render(request, "addcity.html")
    
def city(request):

    lefs = Cities.objects.all()

    return render(request, 'city.html', {'lefs': lefs})