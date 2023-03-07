from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from cojung.models import Problem

def detail(request,problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    context = {'problem':problem}
    return render(request,'cojung/problem.html',context)