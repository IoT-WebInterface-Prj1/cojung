from django.shortcuts import render, redirect, get_object_or_404
from ..models import Question
from..forms import QuestionForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

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

@login_required(login_url='member:login')
def question_modify(request, question_id):
    """
    "Question" 게시글 수정
    """
    question = get_object_or_404(Question, pk = question_id)
    if request.user != question.user:
        messages.error(request, '수정권한이 없습니다 !')
        return redirect('cojung:question_detail', question_id = question.id)
    
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('cojung:question_detail', question_id = question.id)
    else:
        form = QuestionForm(instance=question)
        
    context = {'form' : form}
    
    return render(request, 'cojung/question_form.html', context) 
    
@login_required(login_url='member:login')
def question_delete(request, question_id):
    """
    "Question" 삭제 기능
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.user:
        messages.error(request, '삭제권한이 없습니다 !')
        return redirect('cojung:question_detail', question_id = question.id)
    
    question.delete()
    return redirect('cojung:question')