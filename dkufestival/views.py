from django.shortcuts import render, redirect
from .models import Wirte


def home(request):
    return render(request, 'home.html')


def schedule(request):
    return render(request, 'schedule.html')


def event(request):
    return render(request, 'event.html')


def booth(request):
    return render(request, 'booth.html')


def write(request):
    wirtes = Wirte.objects
    return render(request, 'write.html', {'wirtes': wirtes})


def create(request):
    wirte = Wirte()
    wirte.name = request.GET['name']
    wirte.body = request.GET['body']
    wirte.save()
    return redirect('/festival/write')
