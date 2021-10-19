from django.http import HttpResponse
#import sys
#sys.path.append("fun")
from . import getJS
from django.shortcuts import render


def get_JS(request):
    url = "http://192.168.64.129/"
    proxies = {'http': 'http://127.0.0.1:1181'}
    js_list = getJS.getJSList(url, proxies)
    context = {}
    context['JSList'] = js_list
    return render(request, 'index.html', context)


def hello(request):
    return HttpResponse("<h1>Welcome to UNDEFINED! <h1>")
