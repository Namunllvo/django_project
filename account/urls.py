from django.urls import path
from account import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('user/', views.user_view, name='user-list'),
    # path('user/follow/<int:id>', views.user_follow, name='user-follow'),
]