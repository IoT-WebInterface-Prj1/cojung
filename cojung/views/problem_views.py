from django.contrib.auth import authenticate, login 
from django.shortcuts import render,redirect,get_object_or_404
from cojung.models import Problem
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    pass


def problem_list(request, problem_id):
    problem = Problem.subject.get(id=problem_id)
    context = {'contents':problem}
    return render(request,'cojung/problem.html',context) 


@login_required
def harder(request, Problem_pk):
    if request.user.is_authenticated:
        Problem = get_object_or_404(Problem, pk=Problem_pk)

        if Problem.hard.filter(pk=request.user.pk).exists():
            Problem.hard.remove(request.user)
        else:
            Problem.hard.add(request.user)
        return redirect('cojung:index')
    return redirect('accouts:login')

@login_required
def easyer(request, Problem_pk):
    if request.user.is_authenticated:
        Problem = get_object_or_404(Problem, pk=Problem_pk)

        if Problem.easy.filter(pk=request.user.pk).exists():
            Problem.easy.remove(request.user)
        else:
            Problem.easy.add(request.user)
        return redirect('cojung:index')
    return redirect('accouts:login')