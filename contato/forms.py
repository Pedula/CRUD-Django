from django import forms
from contato.models import Contato


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Contato
