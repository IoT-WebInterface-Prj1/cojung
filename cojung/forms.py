from django import forms
from cojung.models import Resolve, Problem, Answer

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['subject', 'content']

class ResolveForm(forms.ModelForm):
    class Meta:
        model = Resolve
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']