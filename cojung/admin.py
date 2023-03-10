from django.contrib import admin

# Register your models here.
from .models import Problem, Question, Answer, Comment, Language

admin.site.register(Problem)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Language)