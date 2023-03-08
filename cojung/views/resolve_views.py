from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from cojung.forms import ResolveForm
from cojung.models import Problem, Resolve


@login_required
def Resolve_create(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    if request.method == "POST":
        form = ResolveForm(request.POST)
        if form.is_valid():
            resolve = form.save(commit=False)
            resolve.author = request.user  # author 속성에 로그인 계정 저장
            resolve.create_date = timezone.now()
            resolve.problem = problem
            resolve.save()
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'problem': problem, 'form': form}
    return render(request, 'cojung/resolve_list.html', context)

def index(request):

    resolveLst = Resolve.objects.order_by('-create_date')    

    page = request.GET.get('page', '1') #페이지
    paginator = Paginator(resolveLst, 10) #페이지당 10개씩
    
    pageObj = paginator.get_page(page)
    context = {
        'resolveLst' : pageObj, 
    }
    return render(request, 'cojung/resolve_list.html', context)