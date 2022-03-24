from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('absences', views.absences, name='absences-list'),
    path('absences/add', views.addAbsence, name='absence-add')
]