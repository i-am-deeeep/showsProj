from django.shortcuts import render,redirect
from django.http import HttpResponse
from showsApp.models import Shows
from showsApp.forms import ShowsForm


# Create your views here.

def index(request):
    shows=Shows.objects.all()
    return render(request,"showsApp/index.html",context={"shows":shows})

def addShow(request):
    if request.method=="POST":
        form=ShowsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    form=ShowsForm()
    return render(request,"showsApp/addShow.html",{"form":form})
