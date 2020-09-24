"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('join/',views.join, name='join'),
    path('content/',views.content, name='content'),
    path('detail/<int:product_pk>',views.detail, name='detail'),
    path('chat/',views.chat, name='chat'),
    path('trade/',views.trade, name='trade'),
    path('logout/', views.logout, name='logout'),
    path('content_add/', views.content_add, name='content_add'),
]
