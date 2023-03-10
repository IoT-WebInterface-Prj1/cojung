from django.shortcuts import render, get_object_or_404
from cojung.models import Problem, Language
from django.core.paginator import Paginator
from django.db.models import Q, Count

# Create your views here.
def index(request):
    """
    코딩의 정석 "Problem" 목록 출력
    """
    """
    코딩의 정석 "Problem" 목록 출력
    """
    page = request.GET.get('page', '1') #페이지
    # ==============
    # 정렬기능 추가 
    # ==============
    so = request.GET.get('so', 'recent')
    # ==============
    # 검색기능 추가 
    # ==============
    kw = request.GET.get('kw', '')
    # ==============
    # 카테고리 기능 추가 
    # ==============
    langAllLst = Language.objects.all() # 전체 언어 종류
    langLst = request.GET.getlist('lang', '') #선택한 언어 종류

    # ==============
    # 정렬처리
    # ==============
    # problemLst = Problem.objects.order_by('-create_date')   
    if so == 'recent':
        problemLst = Problem.objects.order_by('-create_date')
    elif so == 'hard':
        problemLst = Problem.objects.annotate(num_hard = Count('hard')).order_by('-num_hard', '-create_date')
    elif so == 'easy':
        problemLst = Problem.objects.annotate(num_easy = Count('easy')).order_by('-num_easy', '-create_date')
    elif so == 'resolve':
        problemLst = Problem.objects.annotate(num_resolve = Count('resolve')).order_by('-num_resolve', '-create_date')
    
    # ==============
    # 카테고리 기능 처리 
    # ==============
    if langLst:
        problemLst = Problem.objects.filter(language__name__in = langLst).distinct()
        
    # ==============
    # 조회 처리
    # ==============
    if kw :
        problemLst = problemLst.filter(
            Q(subject__icontains = kw) | #제목검색
            Q(content__icontains = kw) | #내용검색
            Q(user__username__icontains = kw)  #작성자검색
        ).distinct()
    
    # ==============
    # 페이징 처리
    # ==============
    paginator = Paginator(problemLst, 10) #페이지당 10개씩
    
    pageObj = paginator.get_page(page)
    
    # 페이징 기준으로 context 변수 정의
    context = {
        # 'problemLst' : problemLst,
        'problemLst' : pageObj, 
        'page' : page,
        'so' : so, 
        'kw': kw,
        'langAllLst' : langAllLst,
        'langLst' : langLst,
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