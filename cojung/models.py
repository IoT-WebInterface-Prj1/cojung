from django.db import models
from django.contrib.auth.models import User

# 문제
class Problem(models.Model):
    subject = models.CharField('제목', max_length=200)
    content = models.TextField('내용')
    create_date = models.DateTimeField('생성일')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='problem_author')
    #vote
    hard = models.ManyToManyField(User, related_name='vote_hard_problem_user')
    easy = models.ManyToManyField(User, related_name='vote_easy_problem_user')
    # 파일 업로드
    txtfile = models.FileField('첨부파일', null=True, upload_to="media", blank=True)

    def __str__(self):
        return f'{self.subject}'


class Question(models.Model):
    subject = models.CharField('제목', max_length=200)
    content = models.TextField('내용')
    create_date = models.DateTimeField('생성일')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # FK
    problem = models.ForeignKey(Problem, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Problem : {self.problem} / {self.subject}'


class Answer(models.Model):
    content = models.TextField('질문 답변')
    create_date = models.DateTimeField()
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
    
    #ForeignKey
    problem = models.ForeignKey(Problem, on_delete = models.CASCADE)
    
    #Echo ck STR
    def __str__(self):
        return f'{self.problem.subject} {self.problem.content}'

class Comment(models.Model):
    subject = models.CharField(' 제목', max_length = 200)
    content = models.TextField('댓글 내용')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    create_date =  models.DateTimeField('날짜')

    #ForeignKey
    resolve = models.ForeignKey(Resolve, null=True, blank=True, on_delete = models.CASCADE) # 문제 풀이에 대한 Comment
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete = models.CASCADE) # 질문 답변에 대한 Comment
    
    def __str__(self):
        return f'{self.subject}'
