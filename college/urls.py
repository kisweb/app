from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('classes/', views.classe, name='classes'),
    path('classes/list', views.classe_list, name='classe_list'),
    path('classes/add', views.add_classe, name='add_classe'),
    path('classes/<int:pk>/remove', views.remove_classe, name='remove_classe'),
    path('classes/<int:pk>/edit', views.edit_classe, name='edit_classe'),
    path('students/', views.students, name='students'),
    path('students/add', views.add_student, name='add_student'),
    path('students/<int:pk>/edit', views.edit_student, name='edit_student'),
    path('students/<int:pk>/remove', views.remove_student, name='remove_student'),
    path('students/<int:pk>/certificat', views.certificat, name='certificat'),
    path('all_students/', views.ShowAllStudents, name='showStudents'),
    path('show_eleves', views.show_students, name='showEleves'),
    path('create-pdf', views.pdf_report_create, name='create-pdf'),
]