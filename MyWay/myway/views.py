import json
from django.http import JsonResponse
from django.shortcuts import render

def combination_page(request):
    return render(request, 'save_combination.html')

def subway_page(request):
    return render(request, 'subway.html')

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

