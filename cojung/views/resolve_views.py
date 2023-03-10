from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from cojung.forms import ResolveForm,CommentForm
from cojung.models import Problem, Resolve, Comment


@login_required
def Resolve_create(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    if request.method == "POST":
        form = ResolveForm(request.POST)
        if form.is_valid():
            resolve = form.save(commit=False)
            resolve.user = request.user  # author 속성에 로그인 계정 저장
            resolve.create_date = timezone.now()
            resolve.problem = problem
            resolve.save()
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'problem': problem, 'form': form}
    return render(request, 'cojung/resolve_list.html', context)


@login_required(login_url='common:login')
def comment_create_resolve(request, resolve_id):
    """
    pybo 답글댓글등록
    """
    resolve = get_object_or_404(Resolve, pk=resolve_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.create_date = timezone.now()
            comment.resolve = resolve
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('cojung:resolve_detail', problem_id=comment.resolve.problem.id), comment.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'cojung/comment_form.html', context)

def resolve_detail(request,problem_id):
    """
    Problem 게시글
    """
    problem = get_object_or_404(Problem, pk=problem_id)
    context = {'problem':problem}
    return render(request,'cojung/resolve_list.html',context)

@login_required(login_url='common:login')
def resolve_modify(request, resolve_id):
    resolve = get_object_or_404(Resolve, pk=resolve_id)
    if request.user != resolve.user:
        messages.error(request, '수정권한이 없습니다')
        return redirect('cojung:resolve_detail', problem_id=resolve.problem.id)
    if request.method == "POST":
        form = ResolveForm(request.POST, instance=resolve)
        if form.is_valid():
            resovle = form.save(commit=False)
            resolve.modify_date = timezone.now()
            resolve.save()
            return redirect('{}#resolve_{}'.format(
                resolve_url('cojung:resolve_detail', problem_id=resolve.problem.id), resolve.id))
    else:
        form = ResolveForm(instance=resolve)
    context = {'resolve': resolve, 'form': form}
    return render(request, 'cojung/resolve_form.html', context)


@login_required(login_url='common:login')
def resolve_delete(request, resolve_id):
    resolve = get_object_or_404(Resolve, pk=resolve_id)
    if request.user != resolve.user:
        messages.error(request, '삭제권한이 없습니다')
    else:
        resolve.delete()
    return redirect('cojung:resolve_detail', problem_id=resolve.problem.id)