from django.urls import path
from . import views

app_name = 'terrenos'

urlpatterns = [
    path('terrenos/', views.terreno_list, name='terreno_list'),
    path('recursos-naturais/', views.recursos_naturais, name='recursos_naturais'),
    path('documentos/', views.documentos, name='documentos'),
    path('documento_create/', views.documento_create, name='documento_create'),
    path('recurso_natural_create/', views.recurso_natural_create, name='recurso_natural_create'),
    path('gerar_relatorio/', views.gerar_relatorio, name='gerar_relatorio'),
    path('terreno_create/', views.terreno_create, name='terreno_create'),
    path('', views.index, name='index'),  
]
