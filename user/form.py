from django import forms


class AuthenticationForm(forms.Form):
  email = forms.EmailField(max_length=255)
  password = forms.CharField(widget=forms.PasswordInput)
