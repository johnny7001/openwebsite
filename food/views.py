from django.shortcuts import render
from .models import Food, Foodpanda

# Create your views here.
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

import time
from django.template.loader import render_to_string


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




def checknum(request):
    username = request.user.username
    week1 = {
        "國旅券": ["21", "32", "98", "67", "97", "410"],
        "i原券": ["64", "85"],
        "農遊券": ["89", "32", "54", "597", "453", "152"],
        "藝FUN數位": ["96", "15", "07", "30", "73", "98", "19", "11"],
        "藝FUN紙本": ["39", "37", "23", "36", "79", "08", "14", "75"],
        "動滋券": ["97", "13", "19", "55", "71", "93", "381", "734", "644", "453", "985"],
        "客庄券": ["81", "900"],
        "地方創生券": ["081", "105", "594", "188", "089", "396", "521", "467", "912", "798", "358", "441", "367", "941",
                  "335"]}

    # 順序 國旅, I原, 農遊, 藝FUN數位, 藝FUN紙本, 動滋, 客庄, 地方創生

    week2 = {"國旅券": ["87", "04", "40", "29", "71"],
             "i原券": ["12", "59"],
             "農遊券": ["50", "13"],
             "藝FUN數位": ["78", "00", "39", "22", "61", "23", "15"],
             "藝FUN紙本": ["37", "76", "31", "06", "51", "65", "81"],
             "動滋券": ["91", "11", "04", "18", "57", "498", "756"],
             "客庄券": ["11", "439", "841", "052", "206", "161", "457", "205", "012", "293", "446", "589"],
             "地方創生券": ["598", "880", "886", "675", "684", "568", "645", "456"]
             }
    week3 = {"國旅券": ["44", "34", "09", "55", "35", "041"],
            "i原券": ["48", "49"],
            "農遊券": ["60", "75"],
            "藝FUN數位": ["01", "92", "19", "23", "79", "95", "48", "46"],
            "藝FUN紙本": ["31", "56", "02", "52", "44", "49", "00", "47", "59"],
            "動滋券": ["82", "45", "57", "53", "00", "546", "855","865", "012", "983"],
            "客庄券" : ["14","269"],
            "地方創生券" : ["771","706","064","168","191","459","135","314","366"]
    }

    week4 = {"國旅券": ["32", "02", "87", "93", "82", "17"],
            "i原券": ["29", "82" , "71"],
            "農遊券": ["315", "740","381", "264","285", "765","682", "763","373", "015","374"],
            "藝FUN數位": ["70", "61", "37", "85", "67", "35", "44"],
            "藝FUN紙本": ["75", "72", "71", "28", "67", "82", "93", "56", "34", "07"],
            "動滋券": ["30", "03", "51", "88"],
            "客庄券" : ["69"],
            "地方創生券" : ["743","201","119","828","221","750","046"]
    }

    result_list = list()
    num = ""
    if 'num3' in request.GET:
        num = request.GET['num3']

        for item in week1: #key迴圈
            if num in week1[item] or str(num)[1:] in week1[item]:
                result = "恭喜中獎, 第一週{}".format(item)
                result_list.append(result)
                break  #當週如果已經中獎的話, 因為後面中獎其他券種會失效, 所以直接跳出迴圈
            else:
                pass

        for item in week2:
            if num in week2[item] or str(num)[1:] in week2[item]:
                result = "恭喜中獎, 第二週{}".format(item)
                result_list.append(result)
                break
            else:
                pass

        for item in week3:
            if num in week3[item] or str(num)[1:] in week3[item]:
                result = "恭喜中獎, 第三週{}".format(item)
                result_list.append(result)
                break
            else:
                pass

        for item in week4:
            if num in week4[item] or str(num)[1:] in week4[item]:
                result = "恭喜中獎, 第四週{}".format(item)
                result_list.append(result)
                break
            else:
                pass
        if result_list == []:
            content = {'result_list':'沒有中獎コツッ...', 'username':username}
            return render(request, 'ticket5.html', content)
        else:
            content = {'result_list':result_list, 'username':username}
            return render(request, 'ticket5.html', content)

    else: #假如都還沒有輸入任何資訊, 先返回頁面
        content = {'username':username}
        return render(request, 'ticket5.html', content)


def food(request):
    select_pay = request.GET.get('pay')

    food_list = Food.objects.filter(city='臺南市') & Food.objects.filter(pay_list=select_pay)

    paginator = Paginator(food_list, 40)
    page = request.GET.get('page')
    try:
        pageContent = paginator.page(page)
    except PageNotAnInteger:
        pageContent = paginator.page(1)
    except EmptyPage:
        pageContent = paginator.page(paginator.num_pages)

    content = {'food_list':pageContent, 'select_pay':select_pay}

    return render(request, 'food.html', content)



def foodpanda(request):
    username = request.user.username
    goods = ""  # 商品名稱
    startP = ""
    endP = ""

    if 'panda' in request.GET:
        goods = request.GET['panda']


        if len(goods) > 0 and len(startP) == 0 and len(endP) == 0:  # if 沒有填價格
            rest_list = Foodpanda.objects.filter(shopname__icontains=goods).order_by(
                '-star')  # 過濾出title裡面有包含goods的商品名稱
        else:
            rest_list = Foodpanda.objects.all().order_by('-star')[:50]

    else:
        rest_list = Foodpanda.objects.all().order_by('-star')[:50]  # -price=遞減排序

    # rest_list = Foodpanda.objects.all().order_by('-star')
    # content = {'rest_list':rest_list}
    # return render(request, 'foodpanda.html', content)

    paginator = Paginator(rest_list, 10)  # 一頁顯示20筆
    current_page = request.GET.get('page')  # 抓取參數=page的值
    if current_page != None:
        paginator = CustomPaginator(current_page, 11, rest_list, 10)
        try:
            pageContent = paginator.page(current_page)

        except PageNotAnInteger:
            pageContent = paginator.page(1)  # if參數值不為數字, 則跳回第一頁

        except EmptyPage:
            pageContent = paginator.page(paginator.num_pages)  # if參數為空值, 跳到最後一頁

        content = {'rest_list': pageContent, 'username':username}  # dict

        return render(request, 'foodpanda.html', content)
    else:
        current_page = 1  # 假如沒有取得page參數, 就預設頁數在第一頁
        paginator = CustomPaginator(current_page, 11, rest_list, 10)  # 一頁顯示20筆
        try:
            pageContent = paginator.page(current_page)

        except PageNotAnInteger:
            pageContent = paginator.page(1)  # if參數值不為數字, 則跳回第一頁

        except EmptyPage:
            pageContent = paginator.page(paginator.num_pages)  # if參數為空值, 跳到最後一頁

        content = {'rest_list': pageContent, 'username': username}  # dict

        return render(request, 'foodpanda.html', content)
