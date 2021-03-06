# Generated by Django 4.0.3 on 2022-03-12 11:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affectation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.CharField(choices=[('2020-2021', '2021'), ('2021-2022', '2022'), ('2022-2023', '2023')], max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(blank=True, max_length=100, null=True)),
                ('prenoms', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('dateNaissance', models.DateField(blank=True, verbose_name='Date de naissance')),
                ('lieuNaissance', models.CharField(blank=True, max_length=200, verbose_name='Lieu de naissance')),
                ('sexe', models.CharField(choices=[('M', 'Homme'), ('F', 'Femme')], max_length=1)),
                ('contact', models.CharField(blank=True, max_length=20, verbose_name='Téléphone')),
                ('fonction', models.CharField(blank=True, choices=[('Principal', 'Principal'), ('Professeur', 'Professeur'), ('Surveillant général', 'Surveillant général'), ('Surveillant', 'Surveillant')], max_length=30, null=True)),
                ('discipline', models.CharField(blank=True, choices=[('LA', 'LA'), ('LHG', 'LHG'), ('LE', 'LE'), ('LP', 'LP'), ('MSP', 'MSP'), ('MSVT', 'MSVT'), ('MUSIQUE', 'MUSIQUE'), ('ART', 'ART'), ('EPS', 'EPS'), ('ANGLAIS', 'ANGLAIS'), ('HG', 'HG'), ('PORTUGAIS', 'PORTUGAIS'), ('ARABE', 'ARABE')], max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classeroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refClasse', models.CharField(choices=[('31', '3è MA'), ('32', '3è MB'), ('41', '4è MA'), ('42', '4è MB'), ('51', '5è MA'), ('52', '5è MB'), ('61', '6è MA'), ('62', '6è MB')], max_length=10, unique=True, verbose_name='Référence')),
                ('libClasse', models.CharField(choices=[('3e M1 A', '3è MA'), ('3e M1 B', '3è MB'), ('4e M1 A', '4è MA'), ('4e M1 B', '4è MB'), ('5e M1 A', '5è MA'), ('5e M1 B', '5è MB'), ('6e M1 A', '6è MA'), ('6e M1 B', '6è MB')], max_length=25, unique=True, verbose_name='Classe')),
                ('niveau', models.CharField(choices=[('Troisième', 'Troisième'), ('Quatrième', 'Quatrième'), ('Cinquième', 'Cinquième'), ('Sixième', 'Sixième')], max_length=25, verbose_name='Niveau')),
                ('nbTables', models.IntegerField(verbose_name='Nombre de tables')),
                ('surveillant', models.CharField(blank=True, max_length=200, verbose_name='Surveillant')),
                ('profPrincipal', models.CharField(blank=True, max_length=200, verbose_name='Prof principal')),
                ('responsable', models.CharField(blank=True, max_length=200, verbose_name='Responsable')),
            ],
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Discipline')),
            ],
        ),
        migrations.CreateModel(
            name='Fonction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Fonction')),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Matière')),
                ('short_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(blank=True, max_length=10)),
                ('prenoms', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('dateNaissance', models.DateField(blank=True, null=True, verbose_name='Date de naissance')),
                ('lieuNaissance', models.CharField(blank=True, max_length=200, null=True, verbose_name='Lieu de naissance')),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=1)),
                ('pere', models.CharField(blank=True, max_length=100, null=True)),
                ('mere', models.CharField(blank=True, max_length=100, null=True)),
                ('tuteur', models.CharField(blank=True, max_length=100, null=True)),
                ('provenance', models.CharField(blank=True, max_length=100, null=True)),
                ('adresse', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('student_photo', models.ImageField(blank=True, default='students/default.png', null=True, upload_to='students/')),
                ('obervations', models.TextField(blank=True, null=True)),
                ('affectations', models.ManyToManyField(related_name='inscription', to='college.affectation')),
            ],
        ),
        migrations.CreateModel(
            name='DemandAbsence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDeb', models.DateField(default=datetime.datetime.today, verbose_name='Début')),
                ('dateFin', models.DateField(default=datetime.datetime.today, verbose_name='Fin')),
                ('heureDeb1', models.TimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='De')),
                ('heureDeb2', models.TimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='De2')),
                ('heureFin1', models.TimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='A')),
                ('heureFin2', models.TimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='A')),
                ('type', models.CharField(blank=True, choices=[('Cérémonie', 'Cérémonie'), ('Séminaire', 'Séminaire'), ('Salaire', 'Salaire'), ('Convenance personnelle', 'Convenance personnelle'), ('Santé', 'Santé')], max_length=25, verbose_name='Type Absence')),
                ('status', models.BooleanField(default=False, verbose_name='Justifiée')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Commentaires')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.agent')),
            ],
        ),
        migrations.AddField(
            model_name='affectation',
            name='classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.classeroom'),
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateAbs', models.DateField(default=datetime.datetime.today, verbose_name='Début')),
                ('heureDeb', models.TimeField(default=datetime.datetime.now, verbose_name='De')),
                ('heureFin', models.TimeField(default=datetime.datetime.now, verbose_name='A')),
                ('type', models.CharField(blank=True, choices=[('Absence', 'ABSENCE'), ('Retard', 'RETARD'), ('Sortie', 'SORTIE')], max_length=25, verbose_name='Type Absence')),
                ('justified', models.BooleanField(default=False, verbose_name='Justifiée')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Commentaires')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.student')),
            ],
        ),
    ]
