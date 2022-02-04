from django.shortcuts import render, redirect
from .models import Klook, Kkday #User
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
from django.http import HttpResponse
from itertools import chain #可以將多個queryset結合成同一個

class CustomPaginator(Paginator):
    def __init__(self, current_page, max_pager_num, *args, **kwargs):
        """
        :param current_page: 當前頁
        :param max_pager_num:最多顯示的頁碼個數
        :param args:
        :param kwargs:
        :return:
        """
        self.current_page = int(current_page)
        self.max_pager_num = max_pager_num
        super(CustomPaginator, self).__init__(*args, **kwargs)

    def page_num_range(self):
        # 當前頁面
        # self.current_page
        # 總頁數
        # self.num_pages
        # 最多顯示的頁碼個數
        # self.max_pager_num
        print(1)
        if self.num_pages < self.max_pager_num:
            return range(1, self.num_pages + 1)
        print(2)
        part = int(self.max_pager_num / 2)
        if self.current_page - part < 1:
            return range(1, self.max_pager_num + 1)
        print(3)
        if self.current_page + part > self.num_pages:
            return range(self.num_pages + 1 - self.max_pager_num, self.num_pages + 1)
        print(4)
        return range(self.current_page - part, self.current_page + part + 1)



def travel(request):
    username = request.user.username
    goods = ""  # 商品名稱
    startP = ""
    endP = ""

    if 'journey' in request.GET:
        goods = request.GET['journey']
        startP = request.GET['startp']
        endP = request.GET['endp']

        if len(goods) > 0 and len(startP) > 0 and len(endP) > 0:  # if 三者皆有
            journey_list = Klook.objects.filter(title__icontains=goods,  # icontains = 包含物
                                            selling_price__gte=startP,  # gte = 大於等於
                                            selling_price__lte=endP).order_by('selling_price')  # lte = 小於等於
            # gte = 大於等於, gt = 大於, lte = 小於等於, lt = 小於
        elif len(goods) == 0 and len(startP) > 0 and len(endP) > 0:  # if 沒有填商品
            journey_list = Klook.objects.filter(selling_price__gte=startP, selling_price__lte=endP).order_by('selling_price')

        elif len(goods) > 0 and len(startP) == 0 and len(endP) == 0:  # if 沒有填價格
            journey_list = Klook.objects.filter(title__icontains=goods).order_by('-selling_price')  # 過濾出title裡面有包含goods的商品名稱
        else:
            journey_list = Klook.objects.all().order_by('-id')[:50]

    else:
        journey_list = Klook.objects.all().order_by('-id')[:50] # -price=遞減排序, 只搜尋50筆資料

    current_page = request.GET.get('page')  # 抓取參數=page的值
    if current_page != None:
        paginator = CustomPaginator(current_page, 11, journey_list, 10)  # 一頁顯示20筆
        try:
            pageContent = paginator.page(current_page)

        except PageNotAnInteger:
            pageContent = paginator.page(1)  # if參數值不為數字, 則跳回第一頁

        except EmptyPage:
            pageContent = paginator.page(paginator.num_pages)  # if參數為空值, 跳到最後一頁

        content = {'journey_list': pageContent, 'journey':goods, 'startp':startP, 'endp':endP, 'username':username}  # dict

        return render(request, 'travel.html', content)
    else:
        current_page = 1  # 假如沒有取得page參數, 就預設頁數在第一頁
        paginator = CustomPaginator(current_page, 11, journey_list, 10)  # 一頁顯示20筆
        try:
            pageContent = paginator.page(current_page)

        except PageNotAnInteger:
            pageContent = paginator.page(1)  # if參數值不為數字, 則跳回第一頁

        except EmptyPage:
            pageContent = paginator.page(paginator.num_pages)  # if參數為空值, 跳到最後一頁

        content = {'journey_list': pageContent, 'journey': goods, 'startp': startP, 'endp': endP, 'username':username}  # dict

        return render(request, 'travel.html', content)






def kkdayTaiwan(request):
    username = request.user.username
    goods = ""  # 商品名稱
    startP = ""
    endP = ""
    choice_city = ""
    if 'journey' in request.GET:
        goods = request.GET['journey']
        startP = request.GET['startp']
        endP = request.GET['endp']
        choice_city = request.GET['select_city']

#Kkdaychanghua, Kkdaychiayi, Kkdaygreenisland, Kkdayhsinchu, Kkdayhualien, Kkdaykaohsiung, Kkdaykeelung, Kkdaykenting, Kkdaykinmen, Kkdaylanyu,Kkdayliouciou, Kkdaymatzu, Kkdaymiaoli, Kkdaynantou, Kkdaynewtaipeicity, Kkdaykenting, Kkdaypingtung, Kkdaypingxi, Kkdaytaichung, KkdayTainan, Kkdaytaipei, Kkdaytaitung, Kkdaytaoyuan, Kkdayyilan, Kkdayyunlin


        if len(goods) > 0 and len(startP) > 0 and len(endP) > 0 and len(choice_city) > 0: # if 四者皆有
            taiwan_list = Kkday.objects.filter(title__icontains=goods,  # icontains = 包含物
                                                selling_price__gte=startP,  # gte = 大於等於
                                                selling_price__lte=endP, city__icontains=choice_city).order_by('id')  # lte = 小於等於

            # gte = 大於等於, gt = 大於, lte = 小於等於, lt = 小於
        elif len(goods) == 0 and len(startP) > 0 and len(endP) > 0 and len(choice_city) > 0:  # if 沒有填商品

            taiwan_list = Kkday.objects.filter(selling_price__gte=startP, selling_price__lte=endP, city__icontains=choice_city).order_by(
                '-selling_price')


        elif len(goods) > 0 and len(startP) == 0 and len(endP) == 0 and len(choice_city) > 0:  # if 沒有填價格
            taiwan_list = Kkday.objects.filter(title__icontains=goods, city__icontains=choice_city).order_by(
                'id')  # 過濾出title裡面有包含goods的商品名稱

        elif len(goods) > 0 and len(startP) == 0 and len(endP) == 0 and len(choice_city) == 0: #if 沒有選下拉選單
            taiwan_list = Kkday.objects.filter(title__icontains=goods).order_by(
                'id')  # 過濾出title裡面有包含goods的商品名稱

        elif len(goods) == 0 and len(startP) == 0 and len(endP) == 0 and len(choice_city) > 0:  # if 只有下拉選單
            taiwan_list = Kkday.objects.filter(city__icontains=choice_city).order_by(
                'id')  # 過濾出title裡面有包含goods的商品名稱

        elif len(goods) == 0 and len(startP) > 0 and len(endP) > 0 and len(choice_city) == 0:  # if 只有價錢
            taiwan_list = Kkday.objects.filter(selling_price__gte=startP, selling_price__lte=endP).order_by(
                'id')  # 過濾出title裡面有包含goods的商品名稱
        else:
            taiwan_list = Kkday.objects.all().order_by('id')[:50]
    else:
        taiwan_list = Kkday.objects.all().order_by('id')[:50]



    current_page = request.GET.get('page')  # 抓取參數=page的值
    if current_page != None:
        paginator = CustomPaginator(current_page, 11, taiwan_list,  10)  # 一頁顯示20筆
        try:
            pageContent = paginator.page(current_page)

        except PageNotAnInteger:
            pageContent = paginator.page(1)  # if參數值不為數字, 則跳回第一頁

        except EmptyPage:
            pageContent = paginator.page(paginator.num_pages)  # if參數為空值, 跳到最後一頁

        content = {'taiwan_list': pageContent, 'journey': goods, 'startp': startP, 'endp': endP,
                   's_city': choice_city, 'username':username}

        return render(request, 'kkday.html', content)

    else:
        current_page = 1 #假如沒有取得page參數, 就預設頁數在第一頁
        paginator = CustomPaginator(current_page, 11, taiwan_list, 10)  # 一頁顯示20筆
        try:
            pageContent = paginator.page(current_page)

        except PageNotAnInteger:
            pageContent = paginator.page(1)  # if參數值不為數字, 則跳回第一頁

        except EmptyPage:
            pageContent = paginator.page(paginator.num_pages)  # if參數為空值, 跳到最後一頁

        content = {'taiwan_list': pageContent, 'journey': goods, 'startp': startP, 'endp': endP, 's_city': choice_city,
                   'username':username}

        return render(request, 'kkday.html', content)

def kkday_onepage(request):
    username = request.user.username
    goods = ""  # 商品名稱
    startP = ""
    endP = ""
    choice_city = ""
    if 'journey' in request.GET:
        goods = request.GET['journey']
        startP = request.GET['startp']
        endP = request.GET['endp']
        choice_city = request.GET['select_city']

#Kkdaychanghua, Kkdaychiayi, Kkdaygreenisland, Kkdayhsinchu, Kkdayhualien, Kkdaykaohsiung, Kkdaykeelung, Kkdaykenting, Kkdaykinmen, Kkdaylanyu,Kkdayliouciou, Kkdaymatzu, Kkdaymiaoli, Kkdaynantou, Kkdaynewtaipeicity, Kkdaykenting, Kkdaypingtung, Kkdaypingxi, Kkdaytaichung, KkdayTainan, Kkdaytaipei, Kkdaytaitung, Kkdaytaoyuan, Kkdayyilan, Kkdayyunlin


        if len(goods) > 0 and len(startP) > 0 and len(endP) > 0 and len(choice_city) > 0: # if 四者皆有
            taiwan_list = Kkday.objects.filter(title__icontains=goods,  # icontains = 包含物
                                                selling_price__gte=startP,  # gte = 大於等於
                                                selling_price__lte=endP, city__icontains=choice_city).order_by('id')  # lte = 小於等於

            # gte = 大於等於, gt = 大於, lte = 小於等於, lt = 小於
        elif len(goods) == 0 and len(startP) > 0 and len(endP) > 0 and len(choice_city) > 0:  # if 沒有填商品

            taiwan_list = Kkday.objects.filter(selling_price__gte=startP, selling_price__lte=endP, city__icontains=choice_city).order_by(
                '-selling_price')


        elif len(goods) > 0 and len(startP) == 0 and len(endP) == 0 and len(choice_city) > 0:  # if 沒有填價格
            taiwan_list = Kkday.objects.filter(title__icontains=goods, city__icontains=choice_city).order_by(
                'id')  # 過濾出title裡面有包含goods的商品名稱

        elif len(goods) > 0 and len(startP) == 0 and len(endP) == 0 and len(choice_city) == 0: #if 沒有選下拉選單
            taiwan_list = Kkday.objects.filter(title__icontains=goods).order_by(
                'id')  # 過濾出title裡面有包含goods的商品名稱

        elif len(goods) == 0 and len(startP) == 0 and len(endP) == 0 and len(choice_city) > 0:  # if 只有下拉選單
            taiwan_list = Kkday.objects.filter(city__icontains=choice_city).order_by(
                'id')  # 過濾出title裡面有包含goods的商品名稱

        elif len(goods) == 0 and len(startP) > 0 and len(endP) > 0 and len(choice_city) == 0:  # if 只有價錢
            taiwan_list = Kkday.objects.filter(selling_price__gte=startP, selling_price__lte=endP).order_by(
                'id')  # 過濾出title裡面有包含goods的商品名稱
        else:
            taiwan_list = Kkday.objects.all().order_by('id')
    else:
        taiwan_list = Kkday.objects.all().order_by('id')



    current_page = request.GET.get('page')  # 抓取參數=page的值

    content = {'taiwan_list': taiwan_list, 'journey': goods, 'startp': startP, 'endp': endP, 's_city': choice_city,
               'username':username}

    return render(request, 'kkday_onepage.html', content)