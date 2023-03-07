from django.shortcuts import render, redirect
from cojung.forms import ProblemForm
from django.utils import timezone

def create_post(request):
    """cojung 글작성"""
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.create_date = timezone.now()
            problem.save()
            return redirect('cojung:index')
    else:
        form = ProblemForm()
        
    return render(request, 'cojung/problem_form.html', {'form': form})