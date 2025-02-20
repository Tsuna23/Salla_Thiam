from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProjetForm, TacheForm, UtilisateurForm
from .models import Projet, Tache
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from .forms import LoginForm

def creer_utilisateur(request):
    if request.method == 'POST':
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('app/form.html') 
    else:
        form = UtilisateurForm()

    return render(request, 'app/form.html', {'form': form})



class UtilisateurListView(ListView):
    model = get_user_model()
    template_name = 'app/utilisateur_list.html'
    context_object_name = 'utilisateurs'

class UtilisateurDetailView(DetailView):
    model = get_user_model()
    #template_name = 'app/utilisateur_detail.html'
    context_object_name = 'utilisateur'


class ProjetListView(ListView):
    model = Projet
    template_name = 'app/projet_list.html'
    context_object_name = 'projets'

class ProjetDetailView(DetailView):
    model = Projet
   # template_name = 'app/projet_detail.html'
    context_object_name = 'projet'


class TacheListView(ListView):
    model = Tache
  #template_name = 'app/tache_list.html'
    context_object_name = 'taches'


class TacheDetailView(DetailView):
    model = Tache
    template_name = 'app/tache_detail.html'
    context_object_name = 'tache'


class CreerProjetView(CreateView):
    model = Projet
    form_class = ProjetForm 
    template_name = 'app/form_projet.html' 
    success_url = reverse_lazy('projet_list') 

class CreerTacheView(CreateView):
    model = Tache
    form_class = TacheForm
    template_name = 'app/creer_tache.html'
    success_url = reverse_lazy('tache_list')

    # Ajout du décorateur pour vérifier que l'utilisateur est connecté
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request  
        return kwargs
    
 

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tache_list') 
            else:
                form.add_error(None, "Identifiants invalides.")
    else:
        form = LoginForm()

    return render(request, 'app/login.html', {'form': form})



