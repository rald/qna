from django.db import models

from django.utils import timezone



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
    is_answer = models.BooleanField()

    def __str__(self):
        return self.choice_text



class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)



class Score(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    score =  models.PositiveIntegerField(default=0)



