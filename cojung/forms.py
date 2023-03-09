from django import forms

from cojung.models import Resolve, Problem, Question, Answer, Comment


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['subject', 'content', 'txtfile']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content', 'txtfile']


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
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

