from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model      # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'account/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None) #=> None의 의미 는 username이 없다면 none에러를 표시해라
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)

        # username = request.POST.get('username', '')
        # password = request.POST.get('password', '')
        # password2 = request.POST.get('password2', '')
        # bio = request.POST.get('bio', '')

        if password != password2:
            # 패스워드가 일치하지 않는다고 알람
            return render(request, 'account/signup.html', {'error': '패스워드를 확인 해 주세요!'})
        else:
            if username == '' or password == '':
                return render(request, 'account/signup.html', {'error': '사용자 이름과 비밀번호는 필수 값 입니다!'})

            exist_user = get_user_model().objects.filter(username=username)
            # exist_user = UserModel.objects.filter(username=username)
            if exist_user:
                return render(request, 'account/signup.html', {'error': '사용자가 존재합니다!'})

            else:
                # new_user = UserModel()
                # new_user.username = username
                # new_user.password = password
                # new_user.bio = bio
                # new_user.save()
                UserModel.objects.create_user(username=username, password=password)
            return redirect('/login')


# account/views.py
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)

        # me = UserModel.objects.get(username=username)  # 사용자 불러오기
        if me is not None:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            # request.session['user'] = me.username  # 세션에 사용자 이름 저장
            auth.login(request, me)
            # return HttpResponse("로그인 성공") # => erps 페이지로 이동 해야함!
            return redirect('/')

        else:                   # 로그인이 실패하면 다시 로그인 페이지를 보여주기
            # return redirect('/sign-in')
            return render(request, 'account/login.html', {'error': '유저이름 혹은 패스워드를 확인 해 주세요!'}) # render 화면에 다시 보여주기


    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'account/login.html')


@login_required         # 사용자가 로그인이 꼭 되어 있어야만 접근이 가능한 함수
def logout(request):
    auth.logout(request)
    return redirect('/')

