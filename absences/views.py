from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from college.models import Student
from .models import Absence, DemandAbsence
from .forms import AbsenceForm

# Create your views here.

def absences(request):
    context = {
        'absences': Absence.objects.all(),
    }

    return render(request, 'absences/liste.html', context)


def addAbsence(request):
    if request.method == "POST":
        form = AbsenceForm(request.POST)
        if form.is_valid():
            absence = form.save()
            messages.success(request, 'Absence enregistrée avec succès.')
            return redirect('absences-list')
    else:
        form = AbsenceForm()
        return render(request, 'absences/absence_form.html', {'form': form,})


def absenceClasse(request, pk):
    student = get_object_or_404(Student, pk=pk)
    pass
