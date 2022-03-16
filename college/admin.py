from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Affectation, Classeroom, Agent, Student, Absence, Discipline, Matiere

from . models import Parametrage


admin.site.register(Parametrage)

class AgentAdmin(ImportExportModelAdmin):
    list_display = (
        'matricule',
        'prenoms',
        'nom',
        'dateNaissance',
        'lieuNaissance',
        'contact',
        'discipline'
        )
    pass


class StudentAdmin(ImportExportModelAdmin):
    list_display = (
        'matricule',
        'prenoms',
        'nom',
        'dateNaissance',
        'lieuNaissance',
        'contact',
        )
    pass

class ClasseroomAdmin(ImportExportModelAdmin):
    list_display = (
        'refClasse',
        'libClasse',
        'surveillant',
        'profPrincipal',
        'responsable',
        )
    pass

admin.site.register(Matiere)
admin.site.register(Discipline)
admin.site.register(Classeroom, ClasseroomAdmin)
admin.site.register(Affectation)
#admin.site.register(Classeroom)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Absence)
