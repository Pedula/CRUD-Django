from django import forms
from login.models import Login


class PerfilForm(forms.ModelForm):
    class Meta:
		model = Login
		fields = ('usuario','senha')
		senha = forms.CharField(widget=forms.PasswordInput, required=True)

class LoginForm(forms.Form):
	usuario = forms.CharField()
	senha = forms.CharField(widget=forms.PasswordInput)
    