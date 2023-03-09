from django.shortcuts import render,redirect,get_object_or_404
from cojung.models import Answer,Resolve
from cojung.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required(login_url='member:login')
def comment_answer_create(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            
            return redirect('cojung:problem_detail', problem_id = answer.question.id)
    else:
        form = CommentForm()
        
    context = {'answer' : answer, 'form' : form}
    
    return render(request, 'cojung/answer_listl.html', context)

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