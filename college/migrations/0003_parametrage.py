# Generated by Django 4.0.3 on 2022-03-14 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_student_classe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametrage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academie', models.CharField(max_length=200)),
                ('ief', models.CharField(max_length=200)),
                ('etablissement', models.CharField(max_length=200)),
                ('adresse', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('chef', models.CharField(max_length=200)),
            ],
        ),
    ]
