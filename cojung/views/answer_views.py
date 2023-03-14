from django.shortcuts import render,redirect,get_object_or_404
from cojung.models import Question, Answer
from cojung.forms import AnswerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

@login_required(login_url='member:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            
            return redirect('cojung:question_detail', question_id = question.id)
    else:
        form = AnswerForm()
        
    context = {'question' : question, 'form' : form}
    return render(request, 'cojung/question_detail.html', context)

@login_required(login_url='member:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    
    if request.user != answer.user:
        messages.error(request, "수정권한이 없습니다! ")
        return redirect("cojung:question_detail", question_id = answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect("cojung:question_detail", question_id = answer.question.id)
    else:
        form = AnswerForm(instance=answer)
        
    context = {'answer' : answer, 'form' : form}
    return render(request, "cojung/answer_modify_form.html", context)

@login_required(login_url='member:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    
    if request.user != answer.user:
        messages.error(request, "삭제권한이 없습니다! ")
        return redirect("cojung:question_detail", question_id = answer.question.id)
    
    answer.delete()
    return redirect('cojung:question_detail', question_id = answer.question.id)