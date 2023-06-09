from django.db import models

# Create your models here.
class Question(models.Model):
    question_next = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)