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
    # context = {'questionLst' : questionLst}
    
    # ==============
    # 페이징 처리
    # ==============
    page = request.GET.get('page', 1)
    
    paginator = Paginator(questionLst, 2)
    pageObj = paginator.get_page(page)
    
    # 페이징 기준으로 context 변수 정의
    context = {
        'questionLst' : pageObj,
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