from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PerfilUsuario

class FormularioCadastroUsuario(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, label='Nome')
    last_name = forms.CharField(max_length=30, required=True, label='Sobrenome')
    telefone = forms.CharField(max_length=15, required=True)
    data_nascimento = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    cidade = forms.CharField(max_length=100, required=True)
    estado = forms.ChoiceField(choices=PerfilUsuario.ESTADOS_BRASIL, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 
                 'first_name', 'last_name', 'telefone', 
                 'data_nascimento', 'cidade', 'estado']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            perfil = PerfilUsuario(
                usuario=user,
                telefone=self.cleaned_data['telefone'],
                data_nascimento=self.cleaned_data['data_nascimento'],
                cidade=self.cleaned_data['cidade'],
                estado=self.cleaned_data['estado']
            )
            perfil.save()
        
        return user