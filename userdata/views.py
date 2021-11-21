from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Profile, Diary #User
from travel.models import Klook, Kkday
from django import template
from mysite import forms
# Create your views here.
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.contrib.sessions.models import Session #處理session
from django.contrib import messages #處理訊息框架 Messages Framework
from django.contrib.auth import authenticate #授權
from django.contrib import auth
from django.contrib.auth.decorators import login_required #登入要求
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def index_travel(request, pid=None, del_pass=None):
    if request.user.is_authenticated: #檢查登入的user是否為授權狀態
        username = request.user.username
        journey_list = Klook.objects.all().order_by('id')[:8]  # 取最新3筆資料
        kkday_list = Kkday.objects.all().order_by('id')[:8]
    messages.get_messages(request) #獲取login的message內容
    return render(request, 'index.html', locals())

@login_required(login_url='/login/') #此動作要需要登入過後才能執行
def userinfo(request): #user資訊
    if request.user.is_authenticated:
        username = request.user.username
        try:
            user = User.objects.get(username=username)
            userinfo = Profile.objects.get(user=user) #找出Profile相對應的user
        except:
            pass

    return render(request, 'userinfo.html', locals())



def login(request):
    if request.session.test_cookie_worked(): #檢查客戶端瀏覽器是否可以接受cookie
        request.session.delete_test_cookie()
        message = "cookie supported!"
    else:
        message = "cookie not supported!"
    request.session.set_test_cookie()

    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active: #假如user是激活的的情況
                    auth.login(request, user) #把user資料存入session中
                    messages.add_message(request, messages.SUCCESS, '成功登入了')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING,"帳號尚未啟用")
            else:
                messages.add_message(request, messages.WARNING, "登入失敗")
        else:
            messages.add_message(request, messages.INFO, "請檢查輸入的欄位內容")
    else:
        login_form = forms.LoginForm()

    return render(request, 'login.html', locals())


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, "成功登出了")
    return redirect('/')



@login_required(login_url='/login/')
def userpost(request):
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)

    if request.method == 'POST':
        user = User.objects.get(username=username)
        diary = Diary(user=user)
        post_form = forms.DiaryForm(request.POST, instance=diary)
        if post_form.is_valid():
            messages.add_message(request, messages.INFO, "記錄已儲存")
            post_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.INFO, "每一個欄位都要填寫...")
    else:
        post_form = forms.DiaryForm()
        # messages.add_message(request, messages.INFO, '每一個欄位都要填寫...')
    return render(request, 'userpost.html', locals())

def postcheck(request, pid=None, del_pass=None):
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email
        try:
            user = User.objects.get(username=username)
            diaries = Diary.objects.filter(user=user).order_by('-ddate')
        except:
            pass
    messages.get_messages(request)
    return render(request, 'postcheck.html', locals())




#首頁第一版
# def index_travel(request):
#     if 'username' in request.session and 'useremail' in request.session:
#         username = request.session['username']
#         useremail = request.session['useremail']
#
#         journey_list = Klook.objects.all().order_by('id')[:8] #取最新3筆資料
#         kkday_list = Kkday.objects.all().order_by('id')[:8]
#         # content = {'journey_list': journey_list, 'kkday_list': kkday_list}
#         # return render(request, 'index.html', content)
#     else:
#         journey_list = Klook.objects.all().order_by('id')[:8]  # 取最新3筆資料
#         kkday_list = Kkday.objects.all().order_by('id')[:8]
#         # content = {'journey_list': journey_list, 'kkday_list': kkday_list}
#         # return render(request, 'index.html', content)
#     return render(request, 'index.html', locals())







#login 第一版
# def login(request):
#     if request.session.test_cookie_worked(): #檢查客戶端瀏覽器是否可以接受cookie
#         request.session.delete_test_cookie()
#         message = "cookie supported!"
#     else:
#         message = "cookie not supported!"
#     request.session.set_test_cookie()
#
#     if request.method == 'POST':
#         login_form = forms.LoginForm(request.POST)
#         if login_form.is_valid():
#             login_name = request.POST['username'].strip()
#             login_password = request.POST['password']
#             try:
#                 user = User.objects.get(name=login_name) #判斷是否已經是會員
#                 if user.password == login_password:
#                     request.session['username'] = user.name
#                     request.session['useremail'] = user.email
#                     messages.add_message(request, messages.SUCCESS, '成功登入了')
#                     return redirect('/') #登入後回到首頁
#                 else:
#                     messages.add_message(request, messages.WARNING,"密碼錯誤，你重新輸入...")
#             except:
#                 messages.add_message(request, messages.WARNING, "找不到使用者")
#         else:
#             messages.add_message(request, messages.INFO, "請檢查輸入的欄位內容")
#     else:
#         login_form = forms.LoginForm()
#
#     return render(request, 'login.html', locals())








#logout第一版
# def logout(request):
#     #如果是登入狀態, 就刪除session並且導回登入頁面
#     if 'username' in request.session:
#         Session.objects.all().delete()
#         return redirect('/login/')
#     return redirect('/')
