from django.contrib.auth.models import AbstractUser
from django.db import models


ROLE_CHOICES = [
    ('etudiant', 'Étudiant'),
    ('professeur', 'Professeur'),
    ('administrateur', 'Administrateur'),
]

class Utilisateur(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='etudiant')

    REQUIRED_FIELDS = ['email', 'role'] 

    def __str__(self):
        return self.username

    @property
    def est_professeur(self):
        return self.role == 'professeur'

    @property
    def est_etudiant(self):
        return self.role == 'etudiant'

    @property
    def est_administrateur(self):
        return self.role == 'administrateur'

# Modèle projet
class Projet(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='projets', limit_choices_to={'role': 'professeur'})
    
    def __str__(self):
        return self.titre


# Modèle tâche
class Tache(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_echeance = models.DateTimeField()  
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='taches')

    def __str__(self):
        return self.titre

