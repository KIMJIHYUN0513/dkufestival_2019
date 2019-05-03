from dkufestival.models import Wirte
import json


def base(request):
    posts = Wirte.objects.all()

    print('쿼리셋: ', posts)  # 얘는 쿼리셋

    # for문을 돌려서 빼내서 원하는 형태로 딕셔너리를 만들자

    posts_dic = {}

    for post in posts:
        posts_dic[post.name] = post.body

    print('딕셔내뤼: ', posts_dic)

    posts_len = len(posts_dic)

    posts_name = posts_dic.keys()
    posts_body = posts_dic.values()

    posts_name_list = list(posts_name)
    posts_body_list = list(posts_body)

    print(posts_name_list)
    print(posts_body_list)

    return {
        'post_name': posts_name_list,
        'post_body': posts_body_list,
        'post_len': posts_len
    }
