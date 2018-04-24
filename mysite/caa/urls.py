from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'<int:curso_id>/', views.dados, name='dados'),
    path(r'<int:dadosaluno_id>/formularios/', views.formularios, name='formularios'),
    path(r'<int:dadosaluno_id>/formularios/<int:disciplina_id>/', views.questionario, name='questionario'),
   ]