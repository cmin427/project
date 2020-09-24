from django.contrib import admin
from .models import newclass,photo,product_info,Document,facedata
# Register your models here.

admin.site.register(newclass)
admin.site.register(photo)
admin.site.register(product_info)
admin.site.register(Document)
admin.site.register(facedata)