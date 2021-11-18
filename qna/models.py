from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User



class Subject(models.Model):
    subject_text = models.CharField(max_length=200)

    def __str__(self):
        return self.subject_text



class Question(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text



class Score(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    score =  models.PositiveIntegerField(default=0)
    items =  models.PositiveIntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.score} out of {self.items}"

