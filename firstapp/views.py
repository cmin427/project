from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

# Create your views here.

ids_list = ['min','yoon']
pw_list = {'min':'1234',"yoon":'234'}

def home(request):
    if request.method =="POST":
        guest_id = request.POST["userid"]        
        guest_pw = request.POST["userpw"]
        if guest_id in ids_list:
            if pw_list[guest_id] == guest_pw:
                return redirect('content')

    return render(request,'home.html')
    
def join(request):
    if request.method == "POST":
        new_name = request.POST["username"]
        new_id = request.POST["userid"]
        new_pw = request.POST["userpw"]
    return render(request,'join.html')

def content(request):
    return render(request,'content.html')

def detail(request):
    return render(request,'detail.html')

def chat(request):
    return render(request,'chat.html')

def trade(request):
    return render(request,'trade.html')

