from django.db import models
from django.contrib.auth.models import User
import os
import config.settings as settings

class Language(models.Model):
    name = models.CharField('언어명',max_length=100)
    
    # print
    def __str__(self):
        return self.name

# 문제
class Problem(models.Model):
    subject = models.CharField('제목', max_length=200)
    content = models.TextField('내용')
    create_date = models.DateTimeField('생성일')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='problem_author')
    modify_date = models.DateTimeField(null=True,blank=True)

    # 파일 업로드
    txtfile = models.FileField('첨부파일', null=True, upload_to="media", blank=True)
    #vote
    hard = models.ManyToManyField(User, null=True, blank=True, related_name='vote_hard_problem_user')
    easy = models.ManyToManyField(User, null=True, blank=True, related_name='vote_easy_problem_user')
    
    #languages
    language = models.ManyToManyField(Language, null = True, blank=True, related_name = 'language')

    def __str__(self):
        return f'{self.subject}'
    
    #게시글 삭제시 파일 삭제
    def delete(self, *args, **kargs):
        if self.txtfile:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.txtfile.path))
        super(Problem, self).delete(*args, **kargs)

class Question(models.Model):
    subject = models.CharField('제목', max_length=200)
    content = models.TextField('내용')
    create_date = models.DateTimeField('생성일')
    modify_date = models.DateTimeField('수정일', null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # FK
    problem = models.ForeignKey(Problem, null=True, blank=True, on_delete=models.CASCADE)
    # 파일 업로드
    txtfile = models.FileField('첨부파일', null=True, upload_to="media", blank=True)
    
    def __str__(self):
        return f'Problem : {self.problem} / {self.subject}'
    
    #게시글 삭제시 파일 삭제
    def delete(self, *args, **kargs):
        if self.txtfile:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.txtfile.path))
        super(Question, self).delete(*args, **kargs)

class Answer(models.Model):
    content = models.TextField('질문 답변')
    create_date = models.DateTimeField('작성일')
    modify_date = models.DateTimeField('수정일', null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
        
    # FK
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Question : {self.question} / {self.content}'

# 문제에 대한 풀이
class Resolve(models.Model):
    subject = models.CharField(' 제목', max_length = 200)
    content = models.TextField('풀이 내용')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    create_date =  models.DateTimeField('날짜')
    modify_date = models.DateTimeField(null=True,blank=True)
    
    #ForeignKey
    problem = models.ForeignKey(Problem, on_delete = models.CASCADE)
    
    #Echo ck STR
    def __str__(self):
        return f'{self.problem.subject} {self.problem.content}'

class Comment(models.Model):
    content = models.TextField('댓글 내용', null = True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    create_date =  models.DateTimeField('날짜')
    subject = models.CharField(' 제목', max_length = 200)
    #ForeignKey
    resolve = models.ForeignKey(Resolve, null=True, blank=True, on_delete = models.CASCADE) # 문제 풀이에 대한 Comment
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete = models.CASCADE) # 질문 답변에 대한 Comment
    modify_date = models.DateTimeField(null=True,blank=True)    
    def __str__(self):
        return f'{self.content}'
