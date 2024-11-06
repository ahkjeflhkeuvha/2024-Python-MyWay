import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Combination
from .forms import UserForm  # UserForm 임포트
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()  # 사용자를 데이터베이스에 저장
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            # 사용자 인증
            user = authenticate(username=username, password=password)
            if user is not None:
                # 로그인
                login(request, user)
                return redirect("main_page")  # 가입 후 리다이렉트할 페이지
            else:
                # 인증 실패 시 처리
                return render(request, "signup.html", {"form": form, "error": "인증 실패"})
    else:
        form = UserForm()
    return render(request, "signup.html", {"form": form})

def combination_page(request):
    return render(request, 'save_combination.html')

def subway_page(request):
    return render(request, 'subway.html')

def choice_page(request):
    return render(request, 'choice.html')

def save_combinations(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_name = data.get("user_name")
        menu_name = data.get("menu_name")
        items = data.get("items")

        print(data)
        # 데이터베이스에 조합 저장
        combination = Combination.objects.create(
            user_name=user_name,
            menu_name=menu_name,
            items=items
        )
        combination.save()

        return JsonResponse({"status": "success", "message": "조합이 성공적으로 저장되었습니다!"})
    return JsonResponse({"status": "fail", "message": "잘못된 요청입니다."})

def save_combination(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        # 예: 세션에 데이터를 저장
        request.session['saved_combis'] = data
        return JsonResponse({"status": "success", "message": "조합이 성공적으로 저장되었습니다!"})
    return JsonResponse({"status": "fail", "message": "잘못된 요청입니다."})

def result_page(request):
    saved_combis = request.session.get('saved_combis', [])
    print(saved_combis)
    return render(request, 'result.html', {'combis': saved_combis})

def mypage(request):
    combinations = list(Combination.objects.all())
    print(combinations)
    
    for combination in combinations:
        print(combination.menu_name)
        print(combination.items)
    
    return render(request, 'mypage.html', {'combis':combinations})

from django.shortcuts import render

def main_page(request):
    combinations = list(Combination.objects.all())
    
    for combination in combinations:
        print(combination.menu_name)
        print(combination.items)
    
    # 템플릿 렌더링
    return render(request, 'mainpage.html', {'combis': combinations})

def yoajung_page(request):
    return render(request, 'yoajung_page.html')