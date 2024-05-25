from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start_quiz/', views.start_quiz, name='start_quiz'),
    path('next_question/', views.next_question, name='next_question'),
    path('check_answer/', views.check_answer, name='check_answer'),
]
