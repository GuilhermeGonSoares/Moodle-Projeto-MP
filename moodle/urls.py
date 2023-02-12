"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from moodle.views import CursoView, ProvaView, QuestoesViews

app_name = 'moodle'

urlpatterns = [
    path('', CursoView.CursoListView.as_view(), name='home'),
    path('curso/<int:pk>/', CursoView.CursoDetailView.as_view(), name='curso-detail'),
    path('questoes/', QuestoesViews.QuestoesListView.as_view(), name='questoes'),
    path('provas/', ProvaView.ProvaListView.as_view(), name='provas'),
    path('provas/<int:prova_id>/', ProvaView.exibirProva, name='exibir-prova'),
    path('provas/<int:prova_id>/corrigir/',
         ProvaView.corrigirProva, name='corrigir-prova'),
    path('provas/<int:prova_id>/alunos/',
         ProvaView.alunos_provas_feitas, name='alunos-provas'),
    path('questoes/create/', QuestoesViews.QuestaoAlternativasCreateView.as_view(),
         name='questoes-create'),
    path('provas/create/', ProvaView.ProvaCreateView.as_view(), name='provas-create'),
    path('provas/finalizar/<int:prova_id>/',
         ProvaView.finalizarProva, name='finalizar-prova'),
    # path('questoes/update/<int:pk>/', QuestoesViews.QuestaoAlternativasUpdateView.as_view(), name='questoes-update'),
    path('provas/update/<int:pk>/',
         ProvaView.ProvaUpdateView.as_view(), name='provas-update'),
    path('questoes/delete/<int:pk>/',
         QuestoesViews.QuestoesDeleteView.as_view(), name='questoes-delete'),

]
