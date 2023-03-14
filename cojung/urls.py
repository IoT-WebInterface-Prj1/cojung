from django.urls import path
from .views import resolve_views, problem_views, question_views, post_views, vote_views, answer_views, comment_views

app_name = 'cojung'

urlpatterns = [
    #Problem Line --
    path('', problem_views.index, name='index'),
    path('problem/<int:problem_id>/',problem_views.detail, name='detail'),
 
    # 어려워요 ,쉬워요 비교문  
    path('problem/hard/<int:problem_id>',vote_views.harder,name='hard'),
    path('problem/easy/<int:problem_id>',vote_views.easyer,name='easy'),
    path('problem/both/<int:problem_id>',vote_views.both,name='both'),
      
    #Question Line --
    path('question/', question_views.question, name = 'question'),
    path('question/<int:question_id>', question_views.question_detail, name = 'question_detail'),

    
    #Answer Line --
    path('answer/create/<int:question_id>', answer_views.answer_create, name = 'answer_create'),

    # 문제 업로드 / 질문 작성
    path('createpost/', post_views.create_post, name='create_post'),
    path('createquestion/', post_views.create_question, name='create_question'),
    
    #Comment Line --
    path('comment/create/<int:answer_id>', comment_views.comment_answer_create, name = 'comment_answer_create'),

    #풀이 생성 ,댓글
    path('resolve/<int:problem_id>/',resolve_views.resolve_detail,name='resolve_detail'),
    path('resolve/<int:problem_id>/',resolve_views.Resolve_create,name='resolve_create'),
    path('comment/create/resolve/<int:resolve_id>',resolve_views.comment_create_resolve,name='comment_create_resolve'),

    # 문제 업로드 / 질문 작성
    path('createquestion2/', post_views.create_question_problem, name='create_question_problem'),
]