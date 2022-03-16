from django.urls import path

from . import views

urlpatterns = [
    path('showstudents/', views.show_students, name='showstudents'),
    path('create-pdf/', views.pdf_report_create, name='create-pdf'),
]