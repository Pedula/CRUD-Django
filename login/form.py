from django import forms
from login.models import Login


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Login
