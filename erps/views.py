from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import ProductForm
from .models import Product
from django.db import transaction


def home(request):
    user = request.user.is_authenticated
    if user:
        render(request, 'erps/home.html')
    else:
        return redirect('/login')


@login_required
def product_list(request):
    # 상품 등록 view
    if request.method == 'GET':
        user = request.user.is_authenticated  # 사용자가 지금 로그인 되어 있냐
        if user:  # 사용자가 있으면
            product_list_ = Product.objects.order_by('name')
            context = {'product_list': product_list_}  # tweet이 생성된 시간을 역순으로 출력해주는 order_by(역순으로 정렬할수 있게 - 붙임)
            return render(request, 'erps/product_list.html',
                          context)  # 딕셔너리 형태로 키값은 product_list, 이 데이터를 화면에 넘긴다=> 저장한 게시물을 읽어와서 erps/product_list.html로 전달
        else:
            return redirect('/login')


@login_required
def product_create(request):
    if request.method == 'POST':
        user = request.user.is_authenticated
        if user:
            form = ProductForm(request.POST)
        # 유효성 검사
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('/erps/list', '저장완료!')

    else:
        form = ProductForm()
    return render(request, 'erps/product_create.html', {'form': form})


# view
@login_required
@transaction.atomic
def inbound_create(request):
    pass
# 상품 입고 view
# 입고 기록 생성

# 입고 수량 조정


# view
@login_required
def inventory(request):
	"""
	inbound_create, outbound_create view에서 만들어진 데이터를 합산합니다.
	Django ORM을 통하여 총 수량, 가격등을 계산할 수 있습니다.
	"""
	# 총 입고 수량, 가격 계산

	# 총 출고 수량, 가격 계산
