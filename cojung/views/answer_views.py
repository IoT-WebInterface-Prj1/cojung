from django.shortcuts import render,redirect,get_object_or_404
from cojung.models import Question
from cojung.forms import AnswerForm
from django.contrib.auth.decorators import login_required
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
