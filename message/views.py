import urllib.parse
import urllib.request
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .models import Message, Post, Mood
from mysite import forms
import json



# Create your views here.
def message(request):
    username = request.user.username
    if "title" in request.POST:
        title = request.POST['title']
        email = request.POST['email']
        content = request.POST['content']

        Message.objects.create(title=title,email=email,
                               content=content) #欄位名稱=變數

    return render(request, 'message.html', locals()) #locals=所有的內容用字典的方式回傳

def user_login(request):

    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
    except:
        urid = None #若沒有輸入則為空值

    if urid != None and urpass == '12345': #驗證是否有輸入id 及 密碼是否為12345
        verified = True
    else:
        verified = False
    return render(request, 'message.html', locals())

def posting(request):
    username = request.user.username
    moods = Mood.objects.filter().all() #全抓
    try:
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_post = request.POST['user_post']
        user_mood = request.POST['mood']
        if user_id != None:  # 建立新的資料，把po文內容插入資料庫
            mood = Mood.objects.get(status=user_mood)
            post = Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
            post.save()
            message = '成功儲存! 請記得你的編輯密碼[{}]!，訊息須經審查後才會顯示。'.format(user_pass)

    except:
        user_id = None
        message = '如要張貼訊息，請確實填寫每一個欄位...'


    # if del_pass and pid:
    #     try:
    #         post = Post.objects.get(id=pid)
    #     except:
    #         post = None
    #     if post:
    #         if post.del_pass == del_pass:
    #             post.delete()
    #             message='資料刪除成功'
    #         else:
    #             message='密碼錯誤'

    return render(request, 'posting.html', locals())


def listing(request):
    username = request.user.username
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = Mood.objects.all()

    return render(request, 'listing.html', locals())

def contact(request):
    username = request.user.username
    if request.method == 'POST': #判斷傳進來的內容是否為POST
        form = forms.ContactForm(request.POST)
        if form.is_valid(): #檢查表單各欄位內容是否輸入正確
            message = "感謝你的來信"
        else:
            message = "請檢察輸入的資料是否正確"
    else:
        form = forms.ContactForm() #如果不是POST就維持現狀

    return render(request, 'contact.html', locals())

def post2db(request):
    username = request.user.username
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid(): #檢查表單各欄位內容是否輸入正確
            recaptcha_response = request.POST.get('g-recaptcha-response') #驗證小工具出現的標籤
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret':settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response':recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            if result['success']:
                message = "你的訊息已儲存, 要等管理員啟用後才看的到"
                post_form.save()
                return HttpResponseRedirect('/') #送出表單後導向回首頁
            else:
                message = 'reCAPTCHA驗證失敗，請在確認.'
        else:
            message = "如要張貼訊息，請確實填寫每一個欄位..."
    else:
        post_form = forms.PostForm()
        message = "如要張貼訊息，請確實填寫每一個欄位..."

    return render(request, 'post2db.html', locals())

