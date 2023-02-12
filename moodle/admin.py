from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from moodle import models
from user.models import User

"""
@package moodle

@brief Define especificações do Django Admin

"""


class UserAdmin(BaseUserAdmin):
    """Define para usuários a página de admin"""
    ordering = ['id']
    list_display = ['email', 'name', 'user_type']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name')}),
        ('Permições', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'user_type'
        )}),
        ('Datas importantes', {'fields': (
            'last_login',
        )})
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'user_type',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )


admin.site.register(User, UserAdmin)


admin.site.register(models.Alternativa)
admin.site.register(models.Departamento)
admin.site.register(models.Aluno)
admin.site.register(models.Professor)
admin.site.register(models.Disciplina)
admin.site.register(models.Inscricao)
admin.site.register(models.Prova)
admin.site.register(models.Questao)
admin.site.register(models.Desempenho)
admin.site.register(models.CadernoResposta)
