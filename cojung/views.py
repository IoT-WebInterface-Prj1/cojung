from django.shortcuts import render, redirect
from .forms import ProblemForm
from django.utils import timezone

# Create your views here.
def index(request):
    pass

def create_post(request):
    """cojung 글작성"""
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=Flase)
            problem.create_date = timezone.now()
            problem.save()
            return redirect('cojung:index')
    else:
        form = ProblemForm()
        
    return render(request, 'cojung/problem_form.html', {'form': form})