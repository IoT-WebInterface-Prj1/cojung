from django.shortcuts import render, get_object_or_404
from .models import Problem
from django.db.models import Q, Count
from django.core.paginator import Paginator

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

# def problem_detail(request, problem_id):
#     """
#     코딩의 정석 "Problem" 게시글 내용 출력
#     """
#     problem = get_object_or_404(Problem, pk=problem_id)
#     context = {
#         'problem' : problem
#     }
    
#     return render(request, 'cojung/problem_detail.html', context)