from django.contrib import admin

# Register your models here.


from .models import Profile, Diary


admin.site.register(Profile)
admin.site.register(Diary)
