import json
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from . utils import searchStudents, paginateStudents
from .models import *
from .forms import ClasseForm, StudentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import requests


def home(request):
    return render(request, 'college/home.html', {'page': "Gestion des absences"})


def params(request):
    return {
        'params': Parametrage.objects.first()
    }


def lesclasses(request):
    return {
        'lesclasses': Classeroom.objects.all()
    }


def classe(request):
    return render(request, 'index.html', {'page': "Classes"})


def add_classe(request):
    if request.method == "POST":
        form = ClasseForm(request.POST)
        if form.is_valid():
            classe = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "classeListChanged": None,
                        "showMessage": f"{classe.libClasse} ajoutée avec succès."
                    })
                })
    else:
        form = ClasseForm()
    return render(request, 'classe_form.html', {'form': form,})


def edit_classe(request, pk):
    classe = get_object_or_404(Classeroom, pk=pk)
    if request.method == "POST":
        form = ClasseForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "classeListChanged": None,
                        "showMessage": f"{classe.libClasse} updated."
                    })
                }
            )
    else:
        form = ClasseForm(instance=classe)
    return render(request, 'classe_form.html', {
        'form': form,
        'classe': classe,
    })


@ require_POST
def remove_classe(request, pk):
    classe = get_object_or_404(Classeroom, pk=pk)
    classe.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "classeListChanged": None,
                "showMessage": f"{classe.libClasse} deleted."
            })
        })


def show_students(request):
    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'college/pdf/showInfo.html', context)


def pdf_report_create(request):
    students = Student.objects.all()

    template_path = 'college/pdf/pdfReport.html'

    context = {'students': students, 'parametres': Parametrage.objects.get(pk=1)}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="students_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def classe_list(request):
    return render(request, 'classe_list.html', {
        'classes': Classeroom.objects.all(),
        'page': 'Gestion des classes',
    })


def students(request):
    students, search_query = searchStudents(request)
    custom_range, students = paginateStudents(request, students, 15)

    context = {
        'page': 'Gestion des élèves',
        'students': students,
        'search_query': search_query, 
        'custom_range': custom_range
    }

    return render(request, 'college/students/liste.html', context)


def ShowAllStudents(request):
    
    classe = request.GET.get('classe')

    if classe == None:
        students = Student.objects.order_by('nom').filter(classe__refClasse=classe)
        page_num = request.GET.get("page")
        paginator = Paginator(students, 10)
        try:
            students = paginator.page(page_num)
        except PageNotAnInteger:
            students = paginator.page(1)
        except EmptyPage:
            students = paginator.page(paginator.num_pages)             
    else:
        students = Student.objects.filter(classe__refClasse=classe)
       
    
    classes = Classeroom.objects.all()
    
    context = {
        'students': students,
        'laclasse': Classeroom.objects.get(refClasse=classe)
    }

    return render(request, 'college/students/showStudents.html', context)


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "studentListChanged": None,
                        "showMessage": f"{student.nomComplet} ajoutée avec succès."
                    })
                })
    else:
        form = StudentForm()
    return render(request, 'college/students/student_form.html', {'form': form,})


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "studentListChanged": None,
                        "showMessage": f"{student.nomComplet} updated."
                    })
                }
            )
    else:
        form = StudentForm(instance=student)
    return render(request, 'college/students/student_form.html', {
        'form': form,
        'student': student,
    })


@ require_POST
def remove_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "studentListChanged": None,
                "showMessage": f"{student.nomComplet} deleted."
            })
        })


def certificat(request, pk):
    student = get_object_or_404(Student, pk=pk)
    params = Parametrage.objects.first()
    
    return render(request, 'college/students/certificat.html', {
        'student': student,
        'params': params,
    })


def displaydata(request):
    callapi = requests.get('https://dev.h2prog.com/API_TEST/formations')
    results = callapi.json()
    return render(request, 'college/formations/liste.html',{'formations': results})