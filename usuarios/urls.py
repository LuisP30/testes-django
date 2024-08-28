from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.view_login, name='login'),
    path('cadastro/', views.view_cadastro, name='cadastro'),
    path('logout/', views.view_logout, name='logout')
]
