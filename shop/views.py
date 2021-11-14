from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Shop
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

#Paginator = 分頁, PageNotAnInteger = 當頁數不為整數值, EmptyPage = 當頁數為空值


def index(request):
    shop_list = Shop.objects.all().order_by('-id')[:3] #取最新3筆資料
    content = {'shop_list':shop_list}
    return render(request, 'index.html', content)



def shop(request):
    
    goods = "" #商品名稱
    startP = ""
    endP = ""
    if 'product' in request.GET:
        goods = request.GET['product']
        
        startP = request.GET['startp']
        endP = request.GET['endp']
        
        if len(goods) > 0 and len(startP) > 0 and len(endP) > 0: #if 三者皆有
            shop_list = Shop.objects.filter(title__icontains=goods, #icontains = 包含物
                                            price__gte=startP,  #gte = 大於等於
                                            price__lte=endP).order_by('price')   #lte = 小於等於
            #gte = 大於等於, gt = 大於, lte = 小於等於, lt = 小於
        elif len(goods) == 0 and len(startP) > 0 and len(endP) > 0: #if 沒有填商品
            shop_list = Shop.objects.filter(price__gte=startP,price__lte=endP).order_by('price')
        
        elif len(goods) > 0 and len(startP) == 0 and len(endP) == 0: #if 沒有填價格
            shop_list = Shop.objects.filter(title__icontains=goods).order_by('-price') #過濾出title裡面有包含goods的商品名稱
        else:
            shop_list = Shop.objects.all().order_by('price')
            
    else:
        shop_list = Shop.objects.all().order_by('id') #-price=遞減排序
        
        
        
        
    
    paginator = Paginator(shop_list, 5) #一頁顯示20筆
    page = request.GET.get('page') #抓取參數=page的值
    
    try:
        pageContent = paginator.page(page)
        
    except PageNotAnInteger:
        pageContent = paginator.page(1) #if參數值不為數字, 則跳回第一頁
    
    except EmptyPage:
        pageContent = paginator.page(paginator.num_pages) #if參數為空值, 跳到最後一頁
    
    
    content = {'shop_list':pageContent, 'product':goods, 'startp':startP, 'endp':endP} #dict
     
    return render(request, 'shop.html', content)