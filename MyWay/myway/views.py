import json
import random
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Combination
from .forms import UserForm  # UserForm 임포트
from django.contrib.auth import authenticate, login
from django.db.models import Q


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

from django.shortcuts import redirect
from django.urls import reverse
import json

def search_page(request):
    # POST 요청 처리
    if request.method == 'POST':
        try:
            # JSON 데이터를 로드
            print('POST Request Body:', request.body)
            data = json.loads(request.body)
            search_query = data.get("searchData", "").strip()

            # 검색어가 비어있지 않은 경우에만 필터링
            if search_query:
                print(f"Search Query: {search_query}")
                combination = Combination.objects.filter(
                    Q(menu_name__icontains=search_query) | Q(menu_brand__icontains=search_query)
                )

                # 검색 결과가 있으면 리다이렉트하여 GET 요청으로 처리
                if combination:
                    return redirect(reverse('search_page') + f'?search={search_query}')
                else:
                    print('No matching combinations found')
            
            # 검색어가 없거나, 검색 결과가 없는 경우 전체 반환
            combination = Combination.objects.all()
            print(f"Returning all combinations: {combination}")
            return render(request, 'search.html', {"combi": combination})

        except json.JSONDecodeError:
            print("Invalid JSON format")
            return render(request, 'search.html', {"combi": Combination.objects.all()})
        except Exception as e:
            print(f"Error: {e}")
            return render(request, 'search.html', {"combi": Combination.objects.all()})

    # GET 요청 처리
    else:
        print(f"Non-POST request received: {request.method}")
        search_query = request.GET.get('search', '').strip()
        
        if search_query:
            print(f"Search Query from GET: {search_query}")
            combination = Combination.objects.filter(
                Q(menu_name__icontains=search_query) | Q(menu_brand__icontains=search_query)
            )   
        else:
            combination = Combination.objects.all()
        
        return render(request, 'search.html', {"combi": combination})


def subway_page(request):
    return render(request, 'subway.html')

def choice_page(request):
    return render(request, 'choice.html')

def save_combination(request):
    if request.method == "POST":
        data = json.loads(request.body)
        menu_brand = data.get("menu_brand")
        menu_name = data.get("menu_name")
        items = data.get("items")

        print(data)
        # 데이터베이스에 조합 저장
        combination = Combination.objects.create(
            menu_brand=menu_brand,
            menu_name=menu_name,
            items=items
        )
        combination.save()

        return JsonResponse({"status": "success", "message": "조합이 성공적으로 저장되었습니다!"})
    return JsonResponse({"status": "fail", "message": "잘못된 요청입니다."})

def result_page(request):
    return render(request, 'result.html')

def mypage(request):
    combinations = list(Combination.objects.all())
    
    return render(request, 'mypage.html', {'combis':combinations})


def main_page(request):
    combinations = list(Combination.objects.all())
    
    randomCombi = random.sample(combinations, 5)
    
    
    # 템플릿 렌더링
    return render(request, 'mainpage.html', {'combis': randomCombi})

def yoajung_page(request):
    return render(request, 'yoajung_page.html')

def gongcha_page(request):
    return render(request, 'gongcha_page.html')


