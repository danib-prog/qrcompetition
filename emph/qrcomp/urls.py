from django.urls import path

from . import views

app_name = 'qrcomp'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('register/', views.register, name='register'),
    path('successful_registration/', views.successful_registration, name='successful_registration'),
    path('code/<str:name>/', views.code, name='code'),
    path('code_entry', views.code_entry, name='code_entry'),
    path('transaction/<int:transaction_id>/', views.successful_scan, name='successful_scan'),
]