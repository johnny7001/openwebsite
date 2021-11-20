from django.contrib import admin

# Register your models here.


from .models import Mood, Post, Message

class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'message', 'enabled', 'pub_time')
    ordering = ('-pub_time',)

class MoodAdmin(admin.ModelAdmin):
    list_display = ('status',)


admin.site.register(Post, PostAdmin)
admin.site.register(Mood, MoodAdmin)
admin.site.register(Message) #註冊
