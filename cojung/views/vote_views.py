from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

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