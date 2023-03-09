from django.shortcuts import render, redirect
from cojung.forms import ProblemForm, QuestionForm
from django.utils import timezone

def create_post(request):
    """cojung 글작성"""
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.create_date = timezone.now()
            problem.user = request.user
            problem.save()
            return redirect('cojung:index')
    else:
        form = ProblemForm()
        
    return render(request, 'cojung/problem_form.html', {'form': form})


def create_question(request):
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
