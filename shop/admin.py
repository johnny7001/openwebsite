from django.contrib import admin

# Register your models here.
from .models import Shop

class PostShop(admin.ModelAdmin):
    list_display = ('shop', 'title', 'link', 'img_url', 'price', 'create_data')
admin.site.register(Shop, PostShop) #後臺註冊Product'
