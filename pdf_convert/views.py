from django.shortcuts import render

from inscriptions.models import Student

from django.http import HttpResponse

from django.template.loader import get_template

from xhtml2pdf import pisa

# Create your views here.


def show_students(request):
    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'pdf_convert/showInfo.html', context)



def pdf_report_create(request):
    students = Student.objects.all()

    template_path = 'pdf_convert/pdfReport.html'

    context = {'students': students}

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




