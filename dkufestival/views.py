from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def schedule(request):
    return render(request, 'schedule.html')

def event(request):
    return render(request, 'event.html')

def booth(request):
    return render(request, 'booth.html')

def write(request):
    return render(request, 'write.html')
