from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'product.html') #導向product.html

