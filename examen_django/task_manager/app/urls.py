# app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('projet', views.CreerProjetView.as_view(), name='projet'),
    path('tache/', views.CreerTacheView.as_view(), name='tache/'),
     path('login/', views.login_view, name='login'),
    path('user', views.creer_utilisateur, name='user'),
    #path('projet/<int:pk>/', views.ProjetDetailView.as_view(), name='projet_detail'),
    #path('tache/<int:pk>/', views.TacheDetailView.as_view(), name='tache_detail'),
    #path('projets/', views.ProjetListView.as_view(), name='projet_list'),
    #path('taches/', views.TacheListView.as_view(), name='tache_list'),
]
