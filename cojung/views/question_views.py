from django.shortcuts import render, get_object_or_404
from ..models import Question
from django.db.models import Q, Count
from django.core.paginator import Paginator

# ========
# Question Line
# ========
def question(request):
    """
    코딩의 정석 "Question" 목록 출력
    """
    questionLst = Question.objects.order_by('-create_date')
    
    # ==============
    # 검색기능
    # ==============
    kw = request.GET.get('kw', '')
    problem_num = request.GET.get('problem_num', '')
    # ==============
    # 페이징 처리
    # ==============
    page = request.GET.get('page', 1)
    
    # ==============
    # 검색처리
    # ==============
    #문제 -> 질문으로 넘어온 경우
    if problem_num:
        questionLst = questionLst.filter(
            Q(problem__id__icontains = problem_num)
        ).distinct()
    if kw:
        questionLst = questionLst.filter(
            Q(subject__icontains=kw) | #제목검색
            Q(content__icontains=kw) | #내용검색
            Q(problem__subject__icontains=kw) | #질문의 제목 검색
            Q(user__username__icontains=kw) #작성자검색
        ).distinct()
    
    # ==============
    # 페이징처리
    # ==============
    paginator = Paginator(questionLst, 2)
    pageObj = paginator.get_page(page)
    
    # 페이징 기준으로 context 변수 정의
    context = {
        'questionLst' : pageObj,
        'page' : page,
        'kw' : kw,
        'problem_num' : problem_num,
    }
    
    return render(request, 'cojung/question_list.html', context)

def question_detail(request, question_id):
    """
    코딩의 정석 "Question" 게시글 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question' : question
    }
    
    return render(request, 'cojung/question_detail.html', context)