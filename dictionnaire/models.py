from django.db import models

# Create your models here.
"""Catégorie grammaticale du mot    """
class classeGrammaticale(models.Model):
    abbreviation = models.CharField(max_length=10, unique=True)
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom}"

""" Classe nominale qui permet de connaitre le genre des mots en ETon et est utile pour les accords """
class ClasseNominale(models.Model):
    nom = models.CharField(max_length=100, unique=True)  # Ex: "n", "ba-", "ki-", etc.
    description = models.TextField(blank=True, null=True)  # Explication du rôle de la classe nominale

    def __str__(self):
        return self.nom

class MotEton(models.Model):
    mot_eton = models.CharField(max_length=200)
    pluriel = models.CharField(max_length=200, blank=True, null=True)
    class_grammaticale = models.ForeignKey(classeGrammaticale, on_delete=models.SET_NULL, null=True, blank=True, related_name="mots_eton")
    classe_nominale = models.ForeignKey(ClasseNominale, on_delete=models.SET_NULL, null=True, blank=True, related_name="mots_eton")
    mot_reference = models.ManyToManyField('self',blank=True, symmetrical=False, related_name="references") #voir
    synonyme = models.ManyToManyField('self',blank=True, symmetrical=True)
    prononciation = models.FileField(upload_to='audios/mots/', blank=True, null=True)

    def __str__(self):
        return f"{self.mot_eton}"
    
class Traduction(models.Model):
    mot = models.ForeignKey(MotEton, on_delete=models.CASCADE, related_name="traductions")
    mot_francais = models.CharField(max_length=200)
    definition = models.TextField(blank=True, null=True) #description du mot ou de la chose
    image = models.ImageField(upload_to='images/mots/', blank=True, null=True)
    phrase_eton = models.TextField(blank=True, null=True)
    phrase_francais = models.TextField(blank=True, null=True)
    prononciation = models.FileField(upload_to='audios/phrase/', blank=True, null=True)

    def __str__(self):
        return f"{self.mot}: {self.mot_francais}"
    