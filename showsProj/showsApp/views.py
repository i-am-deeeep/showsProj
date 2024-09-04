from django.shortcuts import render,redirect
from django.http import HttpResponse
from showsApp.models import Shows
from showsApp.forms import ShowsForm
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
@login_required
def index(request):
    shows=Shows.objects.all()
    return render(request,"showsApp/index.html",context={"shows":shows})

@login_required
def addShow(request):
    form=ShowsForm()
    if request.method=="POST":
        form=ShowsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"showsApp/addShow.html",{"form":form})

@login_required
@permission_required('showsApp.delete_shows')
def deleteShow(request,id):
    show=Shows.objects.get(id=id)
    show.delete()
    return redirect("/")

@login_required
def updateShow(request,id):
    show=Shows.objects.get(id=id)
    form=ShowsForm(instance=show)
    if request.method=="POST":
        form=ShowsForm(request.POST,instance=show)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"showsApp/updateShow.html",{"form":form})

def logout_confirmed(request):
    return render(request,"showsApp/logout_confirmed.html")