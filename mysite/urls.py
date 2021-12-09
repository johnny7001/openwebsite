"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from shop.views import index
from news.views import news
from shop.views import shop
from message.views import message, listing, posting, contact, post2db
from food.views import food
from food.views import checknum
from food.views import foodpanda
from sakamichi.views import sakamichi
from travel.views import travel, kkdayTaiwan, kkday_onepage
from userdata.views import index_travel, login, logout, userinfo, userpost, postcheck
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('logout/', logout),
    path('', index_travel),
    path('userinfo/', userinfo),
    path('diary_check/', postcheck),
    path('diary/', userpost),
    path('news/', news),
    path('shop/', shop),
    path('message/', message),
    path('message/list', listing),
    path('message/posting', posting),
    path('message/contact', contact),
    path('message/post2db', post2db),
    path('message/list/<int:pid>/<str:del_pass>', listing),
    path('food/', food),
    path('food/ticket5', checknum),
    path('food/foodpanda', foodpanda),
    path('sakamichi/', sakamichi),
    path('travel/', travel), #klook
    path('travel/kkday', kkdayTaiwan),
    path('kkday_onepage/', kkday_onepage),
    path('captcha/', include('captcha.urls')),
    path('accounts/', include('registration.backends.default.urls')),


]
