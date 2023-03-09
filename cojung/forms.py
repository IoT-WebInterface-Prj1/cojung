from django import forms
from cojung.models import Resolve, Problem, Question,Comment

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }
