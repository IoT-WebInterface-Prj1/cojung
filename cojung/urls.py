from django.urls import path
from .views import resolve_views, problem_views, question_views, post_views, vote_views

app_name = 'cojung'

urlpatterns = [
    #Problem Line --
    path('', problem_views.index, name='index'),
    path('problem/<int:problem_id>/',problem_views.detail, name='detail'),
 
    # 어려워요 ,쉬워요 비교문  
    path('<int:problem_pk>/hard/',vote_views.harder,name='hard'),
    path('<int:problem_pk>/easy/',vote_views.easyer,name='easy'),
    
    #Question Line --
    path('question/', question_views.question, name = 'question'),
    path('question/<int:question_id>', question_views.question_detail, name = 'question_detail'),
    #풀이 생성 
    path('resolve/<int:problem_id>/',resolve_views.Resolve_create,name='resolve_create'),

    # 문제 업로드(메인 화면에서 새글작성)
    path('createpost/', post_views.create_post, name='create_post'),
]