from django import forms
<<<<<<< HEAD
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
=======
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FormRegistro(UserCreationForm):
>>>>>>> 5a07cf1c289e548f0c79e7e5e8f00fd7a886097e
    email = forms.EmailField(required=True)

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ["username", "email", "password1", "password2"]

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto']
=======
        fields = ['username', 'email', 'password1', 'password2']
>>>>>>> 5a07cf1c289e548f0c79e7e5e8f00fd7a886097e
