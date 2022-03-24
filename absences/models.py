from django.db import models
from college.models import Student
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
import uuid

from django.urls import reverse

# Create your models here.


class DemandAbsence(models.Model):
    TYPE = (
        ('Cérémonie', 'Cérémonie'), ('Séminaire', 'Séminaire'), ('Salaire', 'Salaire'), ('Convenance personnelle', 'Convenance personnelle'), ('Santé', 'Santé')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    dateDeb = models.DateField('Début', default=datetime.today)
    dateFin = models.DateField('Fin', default=datetime.today)
    heureDeb1 = models.TimeField('De', default=datetime.now, blank=True, null=True)
    heureDeb2 = models.TimeField('De', default=datetime.now, blank=True, null=True)
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
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    dateAbs = models.DateField('Date', default=datetime.today)
    heureDeb = models.TimeField('De', default=datetime.now)
    heureFin = models.TimeField('A', default=datetime.now)
    type = models.CharField('Type Absence', max_length=25, choices=TYPE)
    justified = models.BooleanField('Justifiée', default=False)
    comment = models.TextField('Commentaires', blank=True, null=True)

    def __str__(self):
        return '%s %s (%s %s)' % (self.student.prenoms, self.student.nom, self.student.classe, self.type)

