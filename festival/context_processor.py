from dkufestival.models import Wirte
import json


def base(request):
    posts = Wirte.objects.all()

    print('쿼리셋: ', posts)  # 얘는 쿼리셋

    # for문을 돌려서 빼내서 원하는 형태로 딕셔너리를 만들자

    posts_dict = {}

    for post in posts:
        posts_dict[post.name] = post.body

    print('딕셔내뤼: ', posts_dict)

    # 이 딕셔너리를 json화 시켜서 템플릿으로 가져간 다음,

    # 거기에서 javascript object로 사용하도록 하자.

    posts_json = json.dumps(posts_dict, ensure_ascii=False)

    print('제이쓴', posts_json)

    return {
        'posts_json': posts_json
    }
