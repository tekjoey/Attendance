from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teacher/', views.teacher, name='teacher'),
    path('student/<str:last_name>', views.student, name='student view')
]