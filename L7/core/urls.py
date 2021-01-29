from django.template.defaulttags import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as djangoViews
from django.contrib.auth import urls as djangoUrls
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("", views.startPage, name="start"),
    path("home/", views.home, name="home"),
    path("login/", views.loginToAcc, name="login"),
    path("logout/", views.logoutFromAcc, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("transfer/", views.transfer, name="transfer"),
    path("transactionsHistory/", views.transactionsHistory, name="transactionsHistory"),
    path("password/", views.changePassword, name='changePassword'),
    # path("hello/", views.HelloView.as_view(), name="hello"),
    path('user/create/', views.CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', views.HelloWorldView.as_view(), name='hello_world'),
    path("history/", views.transactions.as_view(), name="history"),
    path("apitrans/", views.transferApi.as_view(), name="apitrans"),
]
