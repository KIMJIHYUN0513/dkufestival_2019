from django.contrib import admin
from django.urls import path
import dkufestival.views
import game.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dkufestival.views.home, name="home"),

    # 카드뉴스관련
    path('festival/schedule', dkufestival.views.schedule, name="schedule"),
    path('festival/booth', dkufestival.views.booth, name="booth"),
    path('festival/mainstage', dkufestival.views.mainstage, name="mainstage"),
    path('festival/busking', dkufestival.views.busking, name="busking"),
    path('festival/lineup', dkufestival.views.lineup, name="lineup"),
    path('festival/nightmarket', dkufestival.views.nightmarket, name="nightmarket"),

    #
    path('festival/event', dkufestival.views.event, name="event"),
    path('festival/map', dkufestival.views.map, name="map"),
    path('festival/write', dkufestival.views.write,
         name="write"),
    path('festival/create', dkufestival.views.create, name="create"),
    path('festival/createhome', dkufestival.views.create_home, name="create_home"),

    # 게임 인클루드
    path('festival/game', game.views.home, name="game"),
    path('festival/game/stage1', game.views.stage1, name="stage1"),
    path('festival/game/stage2', game.views.stage2, name="stage2"),
    path('festival/game/stage3', game.views.stage3, name="stage3"),
    path('festival/game/stage4', game.views.stage4, name="stage4"),
    path('festival/errorpage', game.views.errorPage, name="error"),
    path('festival/game/hallofthefame',
         game.views.lastStage, name="hallofthefame"),
    path('festival/game/hallofthefame/create_record',
         game.views.create_record, name="create_record"),
    path('festival/game/hallofthefame_',
         game.views.lastStage_redirected, name="lastStage_redirected"),
]
