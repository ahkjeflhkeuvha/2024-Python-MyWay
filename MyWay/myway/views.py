from django.http import JsonResponse
from django.shortcuts import render
import json

def combination_page(request):
    return render(request, 'save_combination.html')

def subway_page(request):
    return render(request, 'subway.html')

def save_combination(request):
    if request.method == "POST":
        # JSON 데이터를 파싱하여 가져옵니다.
        data = json.loads(request.body)
        name = data.get("name", "")
        description = data.get("description", "")

        # 받아온 데이터 출력 (데이터베이스에 저장 가능)
        print("Name:", name)
        print("Description:", description)

        return JsonResponse({"status": "success", "message": "조합이 성공적으로 저장되었습니다!"})

    return JsonResponse({"status": "fail", "message": "잘못된 요청입니다."})
