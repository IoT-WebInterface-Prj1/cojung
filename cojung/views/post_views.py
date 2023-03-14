from django.shortcuts import render, redirect
from cojung.forms import ProblemForm, QuestionForm
from django.utils import timezone

def create_post(request):
    """cojung 글작성"""
    if request.method == 'POST':
        form = ProblemForm(request.POST, request.FILES)
        # 여기서 request.FILES 하고 save 아래에서 하니까 아래 코드 한 줄 필요 없음!
        if form.is_valid():
            problem = form.save(commit=False)
            problem.create_date = timezone.now()
            problem.user = request.user
            # problem.txtfile = request.FILES.get('txtfile') # 파일 업로드
            problem.save()
            # language add
            if len(request.POST.getlist('language', None)) == 1:
                # name="language", value=1  =>  {..., language=1, ...} 뽑아오는 코드
                # 다중 선택일 시 리스트로 반환 [1, 2, 3]  =>  getlist 사용
                # value가 int여야 함 (DB에는 id로 저장되기 때문에)
                problem.language.add(request.POST.get('language', None))
            else:
                languages = request.POST.getlist('language', None)
                for language_num in languages:
                    problem.language.add(language_num)
            return redirect('cojung:index')
    else:
        form = ProblemForm()
        
    return render(request, 'cojung/problem_form.html', {'form': form})


def create_question(request):
    """질문 작성"""
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.user = request.user  # user 정보 입력 안하면 에러 발생
            question.save()
            return redirect('cojung:question')
    else:
        form = QuestionForm()
        
    return render(request, 'cojung/question_form.html', {'form': form})

def create_question_problem(request):
    """질문 작성"""
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.user = request.user  # user 정보 입력 안하면 에러 발생
            question.save()
            return redirect('cojung:question')
    else:
        form = QuestionForm()
        
    return render(request, 'cojung/problem_question_form.html', {'form': form})
