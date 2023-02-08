from django.contrib import admin

from moodle import models

admin.site.register(models.Usuario)
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
