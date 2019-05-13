from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Wirte


def home(request):
    return render(request, 'home.html')

# 카드뉴스들


def schedule(request):
    return render(request, 'cardnews/schedule.html')


def booth(request):
    return render(request, 'cardnews/booth.html')


def mainstage(request):
    return render(request, 'cardnews/mainstage.html')


def busking(request):
    return render(request, 'cardnews/busking.html')

def lineup(request):
    return render(request, 'cardnews/lineup.html')

def nightmarket(request):
    return render(request, 'cardnews/nightmarket.html')


def event(request):
    return render(request, 'event.html')


def map(request):
    return render(request, 'map.html')


def write(request):
    wirtes = Wirte.objects.all().order_by('pk').reverse()
    print(wirtes, 'wirte 함수의 쿼리셋;;')
    return render(request, 'write.html', {'wirtes': wirtes})


def create(request):
    wirte = Wirte()
    wirte.name = request.GET['name']
    wirte.body = request.GET['body']
    wirte.save()
    return redirect('/festival/write')


def create_home(request):
    wirte = Wirte()
    wirte.name = request.GET['name']
    wirte.body = request.GET['body']
    wirte.save()
    return redirect('/')
