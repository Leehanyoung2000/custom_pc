from django.shortcuts import render

import requests
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status
from .models import Monitor, Mouse, Keyboard
from .serializers import MonitorSerializer, MouseSerializer, KeyboardSerializer


# Create your views here.

class SearchProductAPIView(APIView):
    model_map = {
        'monitor': Monitor,
        'mouse': Mouse,
        'keyboard': Keyboard
    }

    def get_serializer_class(self, query):
        if query == 'monitor':
            return MonitorSerializer
        elif query == 'mouse':
            return MouseSerializer
        elif query == 'keyboard':
            return KeyboardSerializer
        return None

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', None)
        
        if not query or query not in self.model_map:
            return Response({"errors": "유효한 제품 타입이 필요합니다. (monitor, mouse, keyboard)"}, status=400)
        
        if not query:
            return Response({"errors": "검색어(query)가 필요합니다."}, status=400)

        # 동적으로 모델 선택
        model = self.model_map[query]
        serializer_class = self.get_serializer_class(query)

        url = f"https://openapi.naver.com/v1/search/shop.json?query={query}&sort=sim&display=20"
        headers = {
            "X-Naver-Client-Id": "",
            "X-Naver-Client-Secret": "",
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise APIException(f"API 호출 오류: {e}")

        items = response.json().get("items", [])

        if not items:
            return Response({"message": "검색 결과가 없습니다."}, status=404)

        saved_items = []
        for item in items:
            data = {
                "title": item.get('title'),
                "price": int(item.get('lprice', 0)),
                "brand": item.get('brand', ''),
                "image_url": item.get('image'),
                "link": item.get('link'),
                "mall_name": item.get('mallName')
            }

            # 모델에 저장
            serializer = serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                saved_items.append(serializer.data)
            else:
                return Response({"errors": serializer.errors}, status=400)

        return Response(saved_items)


class MouseList(APIView):
    def get(self, request):
        mouse = Mouse.objects.all()
        serializer = MouseSerializer(mouse, many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        serializer = MouseSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)