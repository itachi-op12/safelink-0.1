from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil
from .models import Plano

class AssinaturaForm(forms.Form):
    plano_id = forms.ModelChoiceField(
        queryset=Plano.objects.all(),
        widget=forms.HiddenInput()
    )


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto']
