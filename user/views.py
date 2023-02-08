# Create your views here.
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from user.form import AuthenticationForm


def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request=request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('moodle:home')
  else:
    form = AuthenticationForm()
  return render(request, 'moodle/user/login.html', {'form': form})


@login_required(login_url='user:login', redirect_field_name='next')
def logout_user(request):

    if request.POST.get('email') != request.user.email:
        return redirect('user:login')

    logout(request)

    return redirect('user:login')
