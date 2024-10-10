from django.db import models
from django.contrib.auth.models import User

class Employe(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_embauche = models.DateField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Dirigeant(models.Model):
    employe = models.OneToOneField(Employe, on_delete=models.CASCADE)
    droits_supplémentaires = models.BooleanField(default=True)

    def __str__(self):
        return f"Dirigeant: {self.employe.nom} {self.employe.prenom}"

class Conge(models.Model):
    TYPE_CONGE = (
        ('CP', 'Congé Payé'),
        ('RTT', 'Réduction du Temps de Travail'),
        ('MAL', 'Maladie'),
    )
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    type_conge = models.CharField(max_length=3, choices=TYPE_CONGE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=10, default='En attente')

    def __str__(self):
        return f"{self.type_conge} - {self.employe.nom} {self.employe.prenom}"
