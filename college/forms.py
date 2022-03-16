from django import forms
from . models import Classeroom, Student


class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classeroom
        fields = ('refClasse', 'libClasse', 'niveau', 'nbTables', 'surveillant', 'profPrincipal', 'responsable')

        widgets = {
            'refClasse': forms.Select(attrs={'class': 'form-control'}),
            'libClasse': forms.Select(attrs={'class': 'form-control'}),
            'niveau': forms.Select(attrs={'class': 'form-control'}),
            'nbTables': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'surveillant': forms.TextInput(attrs={'class': 'form-control'}),
            'profPrincipal': forms.TextInput(attrs={'class': 'form-control'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = ['Référence', 'Classe', 'Niveau', 'Nombre de tables', 'Surveillant', 'Professeur principal',
                  'Responsable'
        ]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'matricule',
            'prenoms',
            'nom',
            'dateNaissance',
            'lieuNaissance',
            'sexe',
            'pere',
            'mere',
            'tuteur',
            'provenance',
            'adresse',
            'contact',
            'classe',
            'affectations',
            'student_photo',
            'obervations'
        ]

        widgets = {
            'matricule': forms.TextInput(attrs={'class': 'form-control'}),
            'prenoms': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'dateNaissance': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lieuNaissance': forms.TextInput(attrs={'class': 'form-control'}),
            'sexe': forms.Select(attrs={'class': 'form-control'}),
            'pere': forms.TextInput(attrs={'class': 'form-control'}),
            'mere': forms.TextInput(attrs={'class': 'form-control'}),
            'tuteur': forms.TextInput(attrs={'class': 'form-control'}),
            'provenance': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'classe': forms.Select(attrs={'class': 'form-control'}),
            'affectations': forms.SelectMultiple(attrs={'class': 'form-control'}),
            #'student_photo': forms.FileField(),
            'obervations': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'matricule': 'Saisir le matricule : ',
            'prenoms': 'Entrer le prénom : ',
            'nom': 'Entrer le nom de famille : ',
            'dateNaissance': 'Saisir la date de naissance : ',
            'lieuNaissance': 'Saisir le lieu de naissance : ',
            'sexe': 'Choisir le sexe : ',
            'pere': 'Prénoms du père : ',
            'mere': 'Nom complet de la mère : ',
            'tuteur': 'Qui est le tuteur, éventuellement ?: ',
            'provenance': 'Ecole de provenance : ',
            'adresse': 'Adresse exacte : ',
            'contact': 'Numéro de téléphone du tuteur ou du père : ',
            'affectations': 'Choisir la classe : ',
            'student_photo': 'Importer une photo : ',
            'obervations': 'Renseignements sur l\'élève : ',

        }
