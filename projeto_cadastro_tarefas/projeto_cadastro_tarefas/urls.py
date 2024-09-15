from django.urls import path
from app_cadastro_tarefas import views

urlpatterns = [
    #rota, view responsável, nome de referência
    path('', views.cadastro, name='cadastro')
]
