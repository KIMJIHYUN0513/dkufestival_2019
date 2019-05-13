from django.shortcuts import render, redirect
from .models import Record
from django.utils import timezone

# Create your views here.


def errorPage(request):
    return render(request, 'game/errorpage.html')


def home(request):
    return render(request, 'game/home.html')


def stage1(request):
    answer = request.GET['answ']
    if(answer == 'LIKELION' or answer == 'likelion'):
        return render(request, 'game/stage1.html')
    else:
        return redirect('/festival/errorpage')


def stage2(request):
    answer = request.GET['answ2']
    if(answer == 'Dynamic' or answer == 'dynamic'):
        return render(request, 'game/stage2.html')
    else:
        return redirect('/festival/errorpage')


def stage3(request):
    answer = request.GET['answ3']
    if(answer == '1947' or answer == '1 9 4 7'):
        return render(request, 'game/stage3.html')
    else:
        return redirect('/festival/errorpage')


def stage4(request):
    answer = request.GET['answ4']
    if(answer == 'linc+' or answer == 'LINC+' or answer == 'linc +' or answer == 'LINC +' or answer == 'Linc+' or answer == 'Linc +'):
        return render(request, 'game/stage4.html')
    else:
        return redirect('/festival/errorpage')


def lastStage(request):
    # 본의아니게 이걸로 url로 스테이지 넘어가는걸 막을 수 있게 되었다..마치 노린것처럼...
    answer = request.GET['answ_last']
    if(answer == 'COLORFUL' or answer == 'colorful' or answer == 'Colorful'):
        return render(request, 'game/hallofthefame.html')
    else:
        return redirect('/festival/errorpage')


def lastStage_redirected(request):
    records = Record.objects
    return render(request, 'game/hallofthefame.html', {'records': records})


def create_record(request):
    record = Record()
    record.name = request.GET['name']
    record.pub_date = timezone.datetime.now()
    record.body = request.GET['body']
    record.save()
    return redirect('/festival/game/hallofthefame_')
