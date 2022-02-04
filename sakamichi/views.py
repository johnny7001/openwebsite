from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import SakuYoutube
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator


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





def sakamichi(request):
    username = request.user.username
    mv_list = SakuYoutube.objects.all().order_by('id')[:50]

    paginator = Paginator(mv_list, 20)  # 一頁顯示20筆
    current_page  = request.GET.get('page')  # 抓取參數=page的值
    if current_page != None:
        paginator = CustomPaginator(current_page, 11, mv_list, 10)
        try:
            pageContent = paginator.page(current_page)

        except PageNotAnInteger:
            pageContent = paginator.page(1)  # if參數值不為數字, 則跳回第一頁

        except EmptyPage:
            pageContent = paginator.page(paginator.num_pages)  # if參數為空值, 跳到最後一頁

        content = {'mv_list': pageContent, 'username': username}  # dict

        return render(request, 'sakamichi.html', content)

    else:
        current_page = 1  # 假如沒有取得page參數, 就預設頁數在第一頁
        paginator = CustomPaginator(current_page, 11, mv_list, 10)  # 一頁顯示20筆
        try:
            pageContent = paginator.page(current_page)

        except PageNotAnInteger:
            pageContent = paginator.page(1)  # if參數值不為數字, 則跳回第一頁

        except EmptyPage:
            pageContent = paginator.page(paginator.num_pages)  # if參數為空值, 跳到最後一頁

        content = {'mv_list': pageContent, 'username':username}  # dict

        return render(request, 'sakamichi.html', content)
