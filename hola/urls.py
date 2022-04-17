from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola, name="hola"),
    path('html/', views.saludoHTML, name="saludoHTML"),
    # path('<str:nombre>/', views.chao, name="chao"),
    path('<str:nombre>/', views.saludoVariableHTML, name="saludoVariableHTML"),
]
