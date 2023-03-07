from django import forms
from cojung.models import Problem

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['subject', 'content']