from django.urls import path
from . import views

app_name = 'cojung'

urlpatterns = [
    #Problem Line --
    path('', views.index, name='index'),
    # path('<int:problem_id>', views.problem_detail, name='problem_detail'),
    #Question Line --
    path('question/', views.question, name = 'question'),
    path('question/<int:question_id>', views.question_detail, name = 'question_detail'),
]