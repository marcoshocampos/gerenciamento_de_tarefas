from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app_cadastro_tarefas import views

urlpatterns = [
    #rota, view responsável, nome de referência
    path('', views.cadastro, name='cadastro')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )