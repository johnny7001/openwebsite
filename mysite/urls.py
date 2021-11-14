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
from message.views import message
from food.views import food
from food.views import checknum
from food.views import foodpanda
from sakamichi.views import sakamichi
from travel.views import travel, index_travel, kkdayTaiwan
urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', index), #導入product裡面的index
    path('', index_travel),
    path('', index),
    path('news/', news),
    path('shop/', shop),
    path('message/', message),
    path('food/', food),
    path('food/ticket5', checknum),
    path('food/foodpanda', foodpanda),
    path('sakamichi/', sakamichi),
    path('travel/', travel), #klook
    path('travel/kkday', kkdayTaiwan),

]
