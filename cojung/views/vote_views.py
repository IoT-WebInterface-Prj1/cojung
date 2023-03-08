from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from cojung.models import Resolve
from django.contrib import messages
from cojung.models import Problem

@login_required
def harder(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    if request.user == problem.author:
        messages.error(request, '본인이 작성한 글은 할수 없습니다')
    else:    
        if  problem.hard.filter(username=request.user.username).exists():
            problem.hard.remove(request.user)
        else:
            problem.hard.add(request.user)
        return redirect('cojung:detail', problem_id=problem.id)
    return redirect('cojung:detail', problem_id=problem.id)

@login_required
def easyer(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    if request.user == problem.author:
        messages.error(request, '본인이 작성한 글은 할수 없습니다')
    else:    
        if  problem.easy.filter(username=request.user.username).exists():
            problem.easy.remove(request.user)
        else:
            problem.easy.add(request.user)
        return redirect('cojung:detail', problem_id=problem.id)
    return redirect('cojung:detail', problem_id=problem.id)
