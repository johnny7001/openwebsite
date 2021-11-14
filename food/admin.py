from django.contrib import admin

# Register your models here.
from .models import Food, Foodpanda

class PostFood(admin.ModelAdmin):
    list_display = ('shop', 'category', 'zone', 'city', 'area', 'market_address', 'pay_list')

class PostFoodpanda(admin.ModelAdmin):
    list_display = ('shopname', 'star', 'content', 'img', 'shopurl', 'tag', 'delivery')

admin.site.register(Food, PostFood)

admin.site.register(Foodpanda, PostFoodpanda)

