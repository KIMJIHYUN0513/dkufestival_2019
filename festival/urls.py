from django.contrib import admin
from django.urls import path
import dkufestival.views
import game.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dkufestival.views.home, name="home"),
    path('festival/schedule', dkufestival.views.schedule, name="schedule"),
    path('festival/event', dkufestival.views.event, name="event"),
    path('festival/booth', dkufestival.views.booth, name="booth"),
    path('festival/write', dkufestival.views.write,
         name="write"),  # 예를 들어 요런 naming은 적절치 않다고 생각합니다 왜냐하면 글을 쓰는 기능이 방명록에만 있지 않을수도 있기 때문..더 '방명록'이라는 것을 명시해주려면 footprint 정도가 적당하지 않을까
    path('festival/create', dkufestival.views.create, name="create"),
    path('festival/createhome', dkufestival.views.create_home, name="create_home"),

    # 게임 인클루드
    path('festival/game', game.views.home, name="game"),
    path('festival/game/stage2', game.views.stage2, name="stage2"),
    path('festival/game/stage3', game.views.stage3, name="stage3"),
    path('festival/game/stage4', game.views.stage4, name="stage4"),
    path('festival/game/hallofthefame',
         game.views.lastStage, name="hallofthefame"),
    path('festival/game/hallofthefame/create_record',
         game.views.create_record, name="create_record"),
    path('festival/game/hallofthefame_',
         game.views.lastStage_redirected, name="lastStage_redirected"),
]
