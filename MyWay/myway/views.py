import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Combination

def combination_page(request):
    return render(request, 'save_combination.html')

def subway_page(request):
    return render(request, 'subway.html')

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

