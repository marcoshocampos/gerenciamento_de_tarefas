from app_cadastro_tarefas.views import cadastro
from django.urls import path

app_name = 'cadastro_tarefas'

urlpatterns = [
    #rota, view responsável, nome de referência
    path('', cadastro, name='cadastro')
]