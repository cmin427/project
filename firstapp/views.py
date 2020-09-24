from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
    
def join(request):
    return render(request,'join.html')

def content(request):
    return render(request,'content.html')

def detail(request):
    return render(request,'detail.html')

def chat(request):
    return render(request,'chat.html')

def trade(request):
    return render(request,'trade.html')

