from django.urls import path
from . import views

app_name = 'lk_core'

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('healthz/', views.healthz, name='healthz'),
    path('/award/<int:amount>/', views.award_amount, name='award'),
    path('/award/plus10/', views.award_plus10, name='award_plus10'),
]
