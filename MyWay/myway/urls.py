"""
URL configuration for myway project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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


from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("main/", views.main_page, name="main_page"),
    path('search/', views.search_page, name="search_page"),
    path('choice/', views.choice_page, name="choice_page"),
    path("subway/", views.subway_page, name="subway_page"),  # 메인 페이지 URL 패턴
    path('yoajung/', views.yoajung_page, name="yoajung_page"),
    path('gongcha/', views.gongcha_page, name="gongcha_page"),
    path("save_combination/", views.save_combination, name="save_combination"),  # 조합 저장 URL 패턴
    path('result/', views.result_page, name="result_page"),  # 결과 페이지 URL 패턴
    path('mypage/', views.mypage, name="mypage"),
]

