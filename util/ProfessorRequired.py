from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy

"""
Previne usuários a entrarem em partes do site
sem autorização de professor.
"""


class ProfessorRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('user:login')
    redirect_field_name = 'redirect_to'

    def dispatch(self, request, *args, **kwargs):
        if request.user.user_type == 'Aluno':
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        return redirect(self.login_url)
