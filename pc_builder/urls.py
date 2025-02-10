

from django.contrib import admin
from django.urls import path, include

from .views import SearchProductAPIView, MouseList

urlpatterns = [
    path('search-product/', SearchProductAPIView.as_view()),
    path('mouses', MouseList.as_view()),
    
]
