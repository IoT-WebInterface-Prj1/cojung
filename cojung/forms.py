from django import forms
from cojung.models import Resolve, Problem, Question

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['subject', 'content']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']


class ResolveForm(forms.ModelForm):
    class Meta:
        model = Resolve
        fields = ['content']
        labels = {
            'content': '답변내용',
        }
