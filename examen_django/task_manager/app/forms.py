from django import forms
from .models import Projet, Tache
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['titre', 'description', 'utilisateur'] 


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['utilisateur'].queryset = get_user_model().objects.filter(role__in=['professeur', 'etudiant'])


class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['titre', 'description', 'date_echeance', 'projet']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  
        super().__init__(*args, **kwargs)

        if self.request and self.request.user.is_authenticated:
            self.fields['projet'].queryset = Projet.objects.filter(utilisateur=self.request.user)
        else:
     
            self.fields['projet'].queryset = Projet.objects.none()

User = get_user_model()

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'role'] 

    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Identifiants invalides.")
        return cleaned_data
    


