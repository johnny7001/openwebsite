from django.contrib import admin

# Register your models here.
from .models import Klook

class PostKlook(admin.ModelAdmin):
    list_display = ('title', 'star', 'market_price', 'selling_price', 'img_url', 'data_url')

admin.site.register(Klook, PostKlook)


