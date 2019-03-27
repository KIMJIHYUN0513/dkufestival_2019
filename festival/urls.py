from django.contrib import admin
from django.urls import path
import dkufestival.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dkufestival.views.home,name="home"),
    path('festival/schedule',dkufestival.views.schedule,name="schedule"),
    path('festival/event',dkufestival.views.event,name="event"),
    path('festival/booth',dkufestival.views.booth,name="booth"),
    path('festival/write',dkufestival.views.write,name="write"),
    path('festival/create',dkufestival.views.create,name="create"),
]
