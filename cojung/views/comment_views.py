from django.shortcuts import render,redirect,get_object_or_404
from cojung.models import Answer,Comment
from cojung.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
            
            return redirect('cojung:question_detail', question_id = answer.question.id)
    else:
        form = CommentForm()
        
    context = {'answer' : answer, 'form' : form}

    return render(request, 'cojung/answer_listl.html', context)

@login_required(login_url="member:login")
def comment_answer_modify(request, comment_id):
    """
    "Comment" 수정 기능
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.user:
        messages.error(request, "수정권한이 없습니다! ")
        return redirect("cojung:question_detail", question_id = comment.answer.question.id)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.modify_date = timezone.now()
            comment.save()
            
            return redirect("cojung:question_detail", question_id = comment.answer.question.id)
    else:
        form = CommentForm(instance=comment)
        
    context = {
        'comment' : comment,
        'form' : form
    }
    
    return render(request, "cojung/comment_modify_form.html", context)

@login_required(login_url="member:login")
def comment_answer_delete(request, comment_id):
    """
    "Comment" 삭제 기능
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.user != comment.user:
        messages.error(request, "삭제권한이 없습니다! ")
        return redirect("cojung:question_detail", question_id = comment.answer.question.id)
    
    comment.delete()
    return redirect("cojung:question_detail", question_id = comment.answer.question.id)