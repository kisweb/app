# Generated by Django 4.0.3 on 2022-03-20 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_parametrage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandabsence',
            name='student',
        ),
        migrations.DeleteModel(
            name='Absence',
        ),
        migrations.DeleteModel(
            name='DemandAbsence',
        ),
    ]
