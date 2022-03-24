from django import forms
from . models import Absence, DemandAbsence
from college.models import Classeroom, Student


class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = '__all__'
