from django.urls import path

from app import views

urlpatterns = [
    path('',views.index),
    path('cadastro/', views.cadastro),
    path('login/', views.login),
    path('combo/', views.combo),
]