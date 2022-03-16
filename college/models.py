from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
import uuid

from django.urls import reverse

# Create your models here.

SEXES = (('M', 'Homme'), ('F', 'Femme'))

ANNEESCOLAIRES = (('2020-2021', '2021'), ('2021-2022', '2022'), ('2022-2023', '2023'))

FONCTIONS = (
    ('Principal', 'Principal'), 
    ('Professeur', 'Professeur'),
    ('Surveillant général', 'Surveillant général'),
    ('Surveillant', 'Surveillant'),
)
DISCIPLINES = (
    ('LA', 'LA'), ('LHG', 'LHG'), ('LE', 'LE'), ('LP', 'LP'),
    ('MSP', 'MSP'), ('MSVT', 'MSVT'), ('MUSIQUE', 'MUSIQUE'), ('ART', 'ART'),
    ('EPS', 'EPS'), ('ANGLAIS', 'ANGLAIS'), ('HG', 'HG'), ('PORTUGAIS', 'PORTUGAIS'),
    ('ARABE', 'ARABE'),
)


class Matiere(models.Model):
    name = models.CharField(verbose_name='Matière', max_length=100)
    short_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Discipline(models.Model):
    name = models.CharField(verbose_name='Discipline', max_length=50)

    def __str__(self):
        return str(self.name)


class Fonction(models.Model):
    name = models.CharField(verbose_name='Fonction', max_length=100, blank=True)

    def __str__(self):
        return str(self.name)


class Agent(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    matricule = models.CharField(max_length=100, blank=True, null=True)
    prenoms = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    dateNaissance = models.DateField(verbose_name='Date de naissance', blank=True)
    lieuNaissance = models.CharField(max_length=200, verbose_name='Lieu de naissance', blank=True)
    sexe = models.CharField(max_length=1, choices=SEXES)
    contact =  models.CharField(max_length=20, verbose_name='Téléphone', blank=True)
    fonction = models.CharField(max_length=30, blank=True, null=True, choices=FONCTIONS)
    discipline = models.CharField(max_length=30, blank=True, null=True, choices=DISCIPLINES)

    def __str__(self):
        return self.prenoms + ' ' + self.nom


class Classeroom(models.Model):

    REFCLASSES = (
        ('31', '3è MA'),
        ('32', '3è MB'),
        ('41', '4è MA'),
        ('42', '4è MB'),
        ('51', '5è MA'),
        ('52', '5è MB'),
        ('61', '6è MA'),
        ('62', '6è MB'),
    )

    MESCLASSES = (
        ('3e M1 A', '3è MA'),
        ('3e M1 B', '3è MB'),
        ('4e M1 A', '4è MA'),
        ('4e M1 B', '4è MB'),
        ('5e M1 A', '5è MA'),
        ('5e M1 B', '5è MB'),
        ('6e M1 A', '6è MA'),
        ('6e M1 B', '6è MB'),
    )

    NIVEAU = (
        ('Troisième', 'Troisième'), ('Quatrième', 'Quatrième'), ('Cinquième', 'Cinquième'), ('Sixième', 'Sixième')
    )

    refClasse = models.CharField('Référence', max_length=10, unique=True, choices=REFCLASSES)
    libClasse = models.CharField('Classe', max_length=25, choices=MESCLASSES, unique=True)
    niveau = models.CharField('Niveau', max_length=25, choices=NIVEAU)
    nbTables = models.IntegerField('Nombre de tables')
    surveillant = models.CharField('Surveillant', max_length=200, blank=True)
    profPrincipal = models.CharField('Prof principal', max_length=200, blank=True)
    responsable = models.CharField('Responsable', max_length=200, blank=True)

    def __str__(self):
        return self.libClasse


class Affectation(models.Model):
    annee = models.CharField(max_length=9, choices=ANNEESCOLAIRES)
    classe = models.ForeignKey('Classeroom', on_delete=models.CASCADE)

    def __str__(self):
        return self.annee + ' ' + self.classe.libClasse


class Student(models.Model):
    SEXE_VAL = (
        ('M', 'Masculin'),
        ('F', 'Féminin')
    )
    matricule = models.CharField(max_length=10, blank=True)
    prenoms = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    dateNaissance = models.DateField(verbose_name='Date de naissance', blank=True, null=True)
    lieuNaissance = models.CharField(max_length=200, verbose_name='Lieu de naissance', blank=True, null=True)
    sexe = models.CharField(max_length=1, choices=SEXE_VAL)
    pere = models.CharField(max_length=100, blank=True, null=True)
    mere = models.CharField(max_length=100, blank=True, null=True)
    tuteur = models.CharField(max_length=100, blank=True, null=True)
    provenance = models.CharField(max_length=100, blank=True, null=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    student_photo = models.ImageField(blank=True, null=True, default='students/default.png', upload_to='students/')
    classe = models.ForeignKey(Classeroom, null=True, blank=True, on_delete=models.SET_NULL)
    affectations = models.ManyToManyField('Affectation', related_name='inscription')
    obervations = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.prenoms, self.nom)

    def get_absolute_url(self):
        return reverse()

    @property
    def nomComplet(self):
        nomComplet = self.prenoms + ' ' + self.nom
        return nomComplet

    @property
    def peremere(self):
        if self.pere == '' or self.mere == '':
            peremere = 'non définis'
        peremere = self.pere + ' et de ' + self.mere
        return peremere

    @property
    def filiation(self):
        if self.sexe == 'M':
            filiation = 'fils de '
        else:
            filiation = 'fille de '
        return filiation

    @property
    def imageURL(self):
        try:
            url = self.student_photo.url
        except:
            url = ''
        return url


class DemandAbsence(models.Model):
    TYPE = (
        ('Cérémonie', 'Cérémonie'), ('Séminaire', 'Séminaire'), ('Salaire', 'Salaire'), ('Convenance personnelle', 'Convenance personnelle'), ('Santé', 'Santé')
    )
    student = models.ForeignKey('Agent', on_delete=models.CASCADE)
    dateDeb = models.DateField('Début', default=datetime.today)
    dateFin = models.DateField('Fin', default=datetime.today)
    heureDeb1 = models.TimeField('De', default=datetime.now, blank=True, null=True)
    heureDeb2 = models.TimeField('De2', default=datetime.now, blank=True, null=True)
    heureFin1 = models.TimeField('A', default=datetime.now, blank=True, null=True)
    heureFin2 = models.TimeField('A', default=datetime.now, blank=True, null=True)
    type = models.CharField('Type Absence', max_length=25, blank=True, choices=TYPE)
    status = models.BooleanField('Justifiée', default=False)
    comment = models.TextField('Commentaires', blank=True, null=True)

    def __str__(self):
        return '%s %s (%s)' % (self.student.prenoms, self.student.nom, self.type)


class Absence(models.Model):
    TYPE = (
        ('Absence', 'ABSENCE'), ('Retard', 'RETARD'), ('Sortie', 'SORTIE')
    )
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    dateAbs = models.DateField('Début', default=datetime.today)
    heureDeb = models.TimeField('De', default=datetime.now)
    heureFin = models.TimeField('A', default=datetime.now)
    type = models.CharField('Type Absence', max_length=25, blank=True, choices=TYPE)
    justified = models.BooleanField('Justifiée', default=False)
    comment = models.TextField('Commentaires', blank=True, null=True)

    def __str__(self):
        return '%s %s (%s %s)' % (self.student.prenoms, self.student.nom, self.student.classe, self.type)



class Parametrage(models.Model):
    academie = models.CharField(max_length=200)
    ief = models.CharField(max_length=200)
    etablissement = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    chef = models.CharField(max_length=200)

    def __str__(self):
        return self.etablissement