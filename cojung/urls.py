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
    path('question/modify/<int:question_id>', question_views.question_modify, name = 'question_modify'),
    path('question/delete/<int:question_id>', question_views.question_delete, name = 'question_delete'),
    
    #Answer Line --
    path('answer/create/<int:question_id>', answer_views.answer_create, name = 'answer_create'),
    path('answer/modify/<int:answer_id>', answer_views.answer_modify, name = 'answer_modify'),
    path('answer/delete/<int:answer_id>', answer_views.answer_delete, name = 'answer_delete'),

    # 문제 업로드 / 질문 작성
    path('createpost/', post_views.create_post, name='create_post'),
    path('createquestion/', post_views.create_question, name='create_question'),
    
    #Comment Line --
    path('comment/create/<int:answer_id>', comment_views.comment_answer_create, name = 'comment_answer_create'),
    path('comment/modify/<int:comment_id>', comment_views.comment_answer_modify, name = 'comment_answer_modify'),
    path('comment/delete/<int:comment_id>', comment_views.comment_answer_delete, name = 'comment_answer_delete'),

    #풀이 생성 ,댓글
    path('resolve/detail/<int:problem_id>/',resolve_views.resolve_detail,name='resolve_detail'),
    path('resolve/<int:problem_id>/',resolve_views.Resolve_create,name='resolve_create'),
    path('resolve/modify/<int:resolve_id>/', resolve_views.resolve_modify, name='resolve_modify'),
    path('resolve/delete/<int:resolve_id>/', resolve_views.resolve_delete, name='resolve_delete'),
    path('comment/create/resolve/<int:resolve_id>',resolve_views.comment_create_resolve,name='comment_create_resolve'),
    path('createquestion/', post_views.create_question, name='create_question'),
    path('problem/modify/<int:problem_id>/', problem_views.problem_modify, name='problem_modify'),
    path('problem/delete/<int:problem_id>/', problem_views.problem_delete, name='problem_delete'),


    # 문제 업로드 / 질문 작성
    path('createquestion2/<int:problem_id>', post_views.create_question_problem, name='create_question_problem'),
]