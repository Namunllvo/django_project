# erps/models.py
from django.db import models
from account.models import UserModel


# Create your models here.
# model - 상품등록
class Product(models.Model):
    class Meta:
        db_table = "product"
    """
    상품 모델입니다.
    상품 코드, 상품 이름, 상품 설명, 상품 가격, 사이즈 필드를 가집니다.
    """
    code = models.CharField(max_length=32, verbose_name="상품 코드", null=False)
    # 카테고리 만들기(후드티, 바지, 양말 등)
    name = models.CharField(max_length=32, null=False, verbose_name="상품이름")
    description = models.TextField(verbose_name="상품설명", null=False)
    price = models.IntegerField(verbose_name="상품 가격", null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)
    # """
    # choices 매개변수는 Django 모델 필드에서 사용하는 매개변수 중 하나로
    # 해당 필드에서 선택 가능한 옵션을 지정하는 역할을 합니다.
    # 변수를 통해 튜플 리스트를 받으면 첫번째 요소는 실제 DB에 저장되는 값이 되고,
    # 두번째 요소는 사용자가 볼 수 있는 레이블(옵션의 이름)이 됩니다.
    # """
    # ERRORS:
    # erps.Product.description: (fields.E120)
    # CharFields
    # must
    # define
    # a
    # 'max_length'
    # attribute. => CharFields는 max_length 꼭 포함해야함 , TextFields로 변경

    def __str__(self):
        return self.code


    # def save(self, *args, **kwargs):
    #     if not self.id: # 생성시 id가 없음 -> 생성동작
    #         do create
    #     else:
    #         do update


# model - 입고
# 문자열 CharField, TextField
    # 날짜/시간 DateTimeField, DateField, TimeField
    # 숫자 IntegerField, FloatField
    # 다른 테이블과 연결 ForeignKey
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # 입고 모델은 """
# 		입고 모델입니다.
# 		상품, 수량, 입고 날짜, 금액 필드를 작성합니다.
# 		"""
class Inbound(models.Model):
    class Meta:
        db_table = "inbound"

    product = models.ManyToManyField(Product)
    i_amount = models.IntegerField(verbose_name="입고 수량", null=False)
    inbound_at = models.DateTimeField(auto_now_add=True)


# model - 출고
class Outbound(models.Model):
    class Meta:
        db_table = "outbound"
    product = models.ManyToManyField(Product)
    o_amount = models.IntegerField(verbose_name="출고 수량", null=False)
    outbound_at = models.DateTimeField(auto_now_add=True)
    # 코드번호와 수량 입력으로 출고수량을 변화 시킬 수 있어야합니다.
    # 수량이 부족한 경우에는 출고를 할 수 없는 예외처리가 되어있어야 합니다.


# # model - 입/출고 합산기능
class Invetory(models.Model):
    class Meta:
        db_table = "inventory"
    # 창고의 제품과 수량 정보
    # 상품, 수량 필드를 작성
    # 작성한 Product 모델을 onetoone 관계로 작성성
    inbound_amount = models.ForeignKey(Inbound, on_delete=models.CASCADE)
    outbound_amount = models.ForeignKey(Outbound, on_delete=models.CASCADE)
    # inventory_amout = models.IntegerField(inbound_amount - outbound_amount)

