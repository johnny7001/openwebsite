from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import News

def news(request):
    newlist = News.objects.all() #抓出News裡面所有的物件
    content = {'news':newlist} #dict的概念
    
    
    return render(request, 'news.html', content) #導向product.html