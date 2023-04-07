from django.contrib import admin    # 장고에서 admin툴을 사용하겠다
from .models import UserModel   # 생성한 모델 가져오기

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',) # 마지막에 , 안 넣으면 문자열로 인식해요.

admin.site.register(UserModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다