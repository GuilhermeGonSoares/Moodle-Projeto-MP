from django.contrib import admin
from django.urls import include, path

from user import views

"""
@package user
Aqui estão definidas as Urls relacionadas ao login e logout de usuario.
"""

app_name = 'user'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_user, name='logout')

]
