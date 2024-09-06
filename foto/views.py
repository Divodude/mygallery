from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from foto import models
from foto.models import dataset,profile
import os
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
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




def fetch(request,id=None):
    """img=dataset.objects.order_by("Date")
    
    
    
    context={img:img}"""
    if id is None:
        return render(request,"userprofile.html")
    else:
        lis=[]
        dir=os.listdir("static")
        for i in dir:
            lis.append(i)
        

        return render(request,"index.html",{"img":lis,"user":id})



def auth(reuqest):
    
    if reuqest.method=='POST':
        email=reuqest.POST.get("email")
        password=reuqest.POST.get("password")
        try:
            user=User.objects.get(username=email)
        except:
            HttpResponse("error 404")
        user=authenticate(reuqest,username=email,password=password)
        if user is not None:
            login(reuqest,user)
            return fetch(reuqest,reuqest.user)
        else:
            HttpResponse("incorrect credentials")
        return render(reuqest,"index.html")
    return render(reuqest,"userprofile.html")


def uplod(request):
    
    pass



            

               






def album(request):

    v="avesh"
    dr=dataset.objects.filter(event=v)
    reqfiles = [obj.path for obj in dr]
    out=[]
    
    
    bsedir= "static"
    for j in reqfiles:
        files=os.path.join(bsedir,j)
        out.append(files)
    

    return render(request,"album.html",{"path":reqfiles})
    

    #return render(request,"album.html")




