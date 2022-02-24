from django.db import models

# 질문 클래스(테이블) 생성
class Question(models.Model):
    question_text = models.CharField(max_length=200)   # 질문내용
    pub_date = models.DateTimeField()                  # 작성일
