from django import forms

class VerificarLinkForm(forms.Form):
    url = forms.URLField(label="Digite o link para verificar", widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'https://exemplo.com'
    }))
