from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexView, name="home"),
    path('polls/', views.allquestions, name="polls"),
    path('polls/<int:question_id>/', views.details, name="poll"),
    path('polls/<int:question_id>/vote/<int:choice_id>', views.vote, name="vote"),
    path('polls/<int:question_id>/result/', views.results, name='result'),
]

