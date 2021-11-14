from django.contrib import admin

# Register your models here.

from .models import SakuYoutube


class PostSakuYoutube(admin.ModelAdmin):
    list_display = ('title', 'videourl', 'imgurl', 'viewcount', 'likecount', 'dislikecount', 'commentcount', 'uploaddate', 'published_date')

admin.site.register(SakuYoutube, PostSakuYoutube) #註冊SakuYoutube

