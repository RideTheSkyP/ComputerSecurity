"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import django.contrib.auth.views as authViews
from django.contrib.auth.models import User
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from core import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    # path("", authViews.LogoutView.as_view(), name="logout"),
    # path("social-auth/", include("social_django.urls", namespace="social")),
    url(r'^', include('django.contrib.auth.urls')),
    # path("api-auth/", include("rest_framework.urls", namespace='rest_framework')),
    path('api/', include('core.urls'))
    # path('password/reset/', authViews.PasswordResetView.as_view(), name='password_reset'),
    # path('password/reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password/reset/done/', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),

    # path('password/reset/complete/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
