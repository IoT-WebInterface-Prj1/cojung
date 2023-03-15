
from django.shortcuts import render, get_object_or_404, redirect
from cojung.models import Problem, Language
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from cojung.forms import ProblemForm
# Create your views here.
def index(request):
    """
    코딩의 정석 "Problem" 목록 출력
    """
    """
    코딩의 정석 "Problem" 목록 출력
    """
    problemLst = Problem.objects.order_by('-create_date')
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
    # 카테고리 기능 처리 
    # ==============
    print(langLst)
    if langLst:
        problemLst = Problem.objects.filter(language__name__in = langLst).distinct()
            
    # ==============
    # 정렬처리
    # ==============
    if so == 'recent':
        problemLst = problemLst.order_by('-create_date')
    elif so == 'hard':
        problemLst = problemLst.annotate(num_hard = Count('hard')).order_by('-num_hard', '-create_date')
    elif so == 'easy':
        problemLst = problemLst.annotate(num_easy = Count('easy')).order_by('-num_easy', '-create_date')
    elif so == 'resolve':
        problemLst = problemLst.annotate(num_resolve = Count('resolve')).order_by('-num_resolve', '-create_date')
        
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
    paginator = Paginator(problemLst, 9) #페이지당 10개씩
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

@login_required(login_url='member:login')
def problem_modify(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    if request.user != problem.user:
        messages.error(request, '수정권한이 없습니다')
        return redirect('cojung:detail', problem_id=problem.id)
    if request.method == "POST":
        form = ProblemForm(request.POST, request.FILES, instance=problem)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.modify_date = timezone.now()  # 수정일시 저장
            
            #Language Add
            if len(request.POST.getlist('language', None)) == 1:
                # name="language", value=1  =>  {..., language=1, ...} 뽑아오는 코드
                # 다중 선택일 시 리스트로 반환 [1, 2, 3]  =>  getlist 사용
                # value가 int여야 함 (DB에는 id로 저장되기 때문에)
                problem.language.add(request.POST.get('language', None))
            else:
                languages = request.POST.getlist('language', None)
                for language_num in languages:
                    problem.language.add(language_num)
            
            problem.save()
            return redirect('cojung:detail', problem_id=problem.id)
    else:
        form = ProblemForm(instance=problem)

    language_list = Language.objects.all()
    language_select_list = []
    #선택한 언어가 있는 경우 list 추가
    if problem.language:
        for lang in problem.language.all():
            language_select_list.append(lang.name)
            
    context = {
        'form': form, 
        'language_list': language_list,
        'language_select_list' : language_select_list
    }
    return render(request, 'cojung/problem_form.html', context)


@login_required(login_url='member:login')
def problem_delete(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    if request.user != problem.user:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('cojung:detail', problem_id=problem.id)
    problem.delete()
    return redirect('cojung:index')