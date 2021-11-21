from django.contrib import admin

# Register your models here.
from .models import Klook, Kkday

class PostKlook(admin.ModelAdmin):
    list_display = ('title', 'star', 'market_price', 'selling_price', 'img_url', 'data_url')
    search_fields = ('title',) #依名稱搜尋
    ordering = ('-star', '-selling_price',) #增加排序設定
class PostKkday(admin.ModelAdmin):
    list_display = ('city', 'title', 'content', 'rating_count', 'star', 'order_count', 'market_price', 'selling_price', 'img_url', 'data_url')



admin.site.register(Klook, PostKlook)
admin.site.register(Kkday, PostKkday)

