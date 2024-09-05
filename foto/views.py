from django.shortcuts import render,HttpResponse
from datetime import datetime
from foto import models
from foto.models import dataset
import os
# Create your views here.
def home(request):
    return HttpResponse("hi")
def upload(request):
    return HttpResponse("hi")
    """if request.method=="POST":
        event=request.POST.get('event')
        date=datetime.now()
        path="path"
        name=request.POST.get("name")
    return render("userprofile.html")"""




def fetch(request):
    """img=dataset.objects.order_by("Date")
    
    
    context={img:img}"""
    lis=[]
    dir=os.listdir("static")
    for i in dir:
        lis.append(i)

    return render(request,"index.html",{"img":lis})



def auth(reuqest):
    return render(reuqest,"login.html")




def album(request):
    dr=os.listdir("static")
    

    return render(request,"album.html")




