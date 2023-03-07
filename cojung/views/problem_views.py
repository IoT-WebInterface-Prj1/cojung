from django.contrib.auth import authenticate, login 
from django.shortcuts import render,redirect,get_object_or_404
from cojung.models import Problem
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Count

# Create your views here.
def index(request):
    """
    코딩의 정석 "Problem" 목록 출력
    """
    problemLst = Problem.objects.order_by('-create_date')    
    # ==============
    # 페이징 처리
    # ==============
    page = request.GET.get('page', '1') #페이지
    paginator = Paginator(problemLst, 10) #페이지당 10개씩
    
    pageObj = paginator.get_page(page)
    
    # 페이징 기준으로 context 변수 정의
    context = {
        # 'problemLst' : problemLst,
        'problemLst' : pageObj, 
    }
    
    return render(request, 'cojung/problem_list_main.html', context)

def detail(request,problem_id):
    """
    Problem 게시글
    """
    problem = get_object_or_404(Problem, pk=problem_id)
    context = {'problem':problem}
    return render(request,'cojung/problem.html',context)

# def problem_list(request, problem_id):
#     problem = Problem.subject.get(id=problem_id)
#     context = {'contents':problem}
#     return render(request,'cojung/problem.html',context) 