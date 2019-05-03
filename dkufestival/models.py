from django.db import models


class Wirte(models.Model):      # 방명록 모델(Wirte 오타 주의 ㅠㅠ)..
    name = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.name
