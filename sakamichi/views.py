from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import SakuYoutube
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

def sakamichi(request):

    mv_list = SakuYoutube.objects.all().order_by('id')

    paginator = Paginator(mv_list, 20)  # 一頁顯示20筆
    page = request.GET.get('page')  # 抓取參數=page的值

    try:
        pageContent = paginator.page(page)

    except PageNotAnInteger:
        pageContent = paginator.page(1)  # if參數值不為數字, 則跳回第一頁

    except EmptyPage:
        pageContent = paginator.page(paginator.num_pages)  # if參數為空值, 跳到最後一頁

    content = {'mv_list': pageContent}  # dict

    return render(request, 'sakamichi.html', content)
