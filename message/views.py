from django.shortcuts import render

from django.http import HttpResponse
from .models import Message


# Create your views here.
def message(request):
    
    if "title" in request.POST:
        title = request.POST['title']
        email = request.POST['email']
        content = request.POST['content']
        
        Message.objects.create(title=title,email=email,
                               content=content) #欄位名稱=變數
        
    return render(request, 'message.html', locals()) #locals=所有的內容用字典的方式回傳
    