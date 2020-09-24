from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from .models import newclass,photo,product_info
import os
import sys
import requests
from face_recognition import facedetection

#   Create your views here.
#   Create your views here.
ERROR_MSG = {
    'ID_EXIST': '이미 사용 중인 아이디 입니다.',
    'ID_NOT_EXIST': '존재하지 않는 아이디 입니다.',
    'ID_PW_MISSING': '아이디와 비밀번호를 확인해주세요.',
    'PW_CHECK': '비밀번호가 일치하지 않습니다.'
}

ids_list = ['min','yoon']
pw_list = {'min':'1234',"yoon":'234'}

def logout(request):

    auth.logout(request)

    return redirect('index')

def index(request):
    context = {
        'error': {
            'state': False,
            'msg': ''
        }
    }
    if request.method =="POST":
        user_id = request.POST["user_id"]        
        user_pw = request.POST["user_pw"]
        user = User.objects.filter(username=user_id)
        if (user_id and user_pw):
            if len(user) != 0:
                user = auth.authenticate(
                    username=user_id,
                    password=user_pw
                )

                if user != None:
                    auth.login(request, user)

                    return redirect('index')
                else:
                    context['error']['state'] = True
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']
            else:
                context['error']['state'] = True
                context['error']['msg'] = ERROR_MSG['ID_NOT_EXIST']

        else:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']

    return render(request, 'index.html', context)

    
def join(request):
    
    context = {
        'error': {
            'state': False,
            'msg': ''
        }
    }
    if request.method == "POST":

        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_pw_check = request.POST['user_pw_check']

        # # 추가
        # user_HP = int(request.POST['user_HP'])
        # name = request.POST['name']
        # phone_num = request.POST['phone_num']

        if (user_id and user_pw):

            user = User.objects.filter(username=user_id)

            if len(user) == 0:

                if user_pw == user_pw_check:

                    

                    created_user = User.objects.create_user(
                        username=user_id,
                        password=user_pw
                    )
                    face_detected = photo.objects.create(
                        user_id=user_id,
                        photo_num=0
                    )

                    auth.login(request, created_user)

                    return redirect('index')

                else:
                    context['error']['state'] = True
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']
            else:
                context['error']['state'] = True
                context['error']['msg'] = ERROR_MSG['ID_EXIST']

        else:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']

    return render(request, 'join.html', context)    
    if request.method == "POST":
        print(request.POST)
        new_name = request.POST["username"]
        new_id = request.POST["userid"]
        new_pw = request.POST["userpw"]
        new_pw_confirm = request.POST["userpw_confirm"]
        if (new_id and new_pw):
            user = User.objects.filter(username=new_id) 
            if len(user) == 0:
                if (new_pw == new_pw_confirm):
                    # user = User.objects.create_user
                    return render(request,'join.html')
    return render(request,'join.html')

def content(request):
    product = product_info.objects.all()
    context ={'product':product}
    return render(request,'content.html',context)

def content_add(request):
    if request.method =="POST":
        name = request.POST["product_name"]
        price = request.POST["product_price"]
        region = request.POST["product_region"]
    
        product_info.objects.create(
            name=name,
            price=price,
            region=region
        )

        return redirect('content')

    return render(request, 'content_add.html')
    

def detail(request,):
    return render(request,'detail.html')

def chat(request):
    return render(request,'chat.html')

def trade(request):
    return render(request,'trade.html')

