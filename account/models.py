#account/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings        # 장고가 관리하고 있는 설정들을 가져오는것


# Create your models here.
class UserModel(AbstractUser):
    class Meta:     # 데이터 베이스에 정보를 넣어주는 역할
        db_table = "my_user" # 테이블 이름

    # bio = models.CharField(max_length=256, default='')
    # follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')
    # follow는 사용자 정보

    # django 모델 필드의 종료
    # 문자열 CharField, TextField
    # 날짜/시간 DateTimeField, DateField, TimeField
    # 숫자 IntegerField, FloatField
    # 다른 테이블과 연결 ForeignKey
    # username = models.CharField(max_length=20, null=False)
    # password = models.CharField(max_length=256, null=False)
    # bio = models.CharField(max_length=256, default='')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

# makemigrations 하는데
# TypeError: 'module' object is not iterable
# 이런 에러가 생긴다 그래서 해결하려고
# models.Model로 변경했는데 해결안됨 뭐지
# 해결!
# urls파일에 아무것도 없어서 그런거임