from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Student(models.Model):  
    StuName = models.OneToOneField(User)  # this is extending existing user models in Django
    Score = models.IntegerField()




class Teacher(models.Model):
    TeaName = models.OneToOneField(User)    
    
    
    def __str__(self):
        return self.TeaName.username


class QuizSet(models.Model):
    TestName = models.CharField(default='test series', max_length=100)
    No_of_questions = models.IntegerField()
    Marks_for1 = models.IntegerField()
    Time = models.IntegerField()
    Created_Date = models.DateTimeField(default=timezone.now)
    Published_date = models.DateTimeField(blank=True, null=True)
    Author = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def publish(self):
        self.Published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.TestName


class Question(models.Model):
    quizset = models.ForeignKey(QuizSet, on_delete=models.CASCADE)  # Question belongs to QuizSet
    QText = models.CharField(max_length=200)
    AText = models.CharField(max_length=50)
    Author = models.ForeignKey(Teacher, on_delete=models.CASCADE)     # Teacher = author
    
    def __str__(self):
        return self.QText[:15]


class AnswerSet(models.Model):
    Qno = models.ForeignKey(Question, on_delete=models.CASCADE)
    AText = models.CharField(max_length=50)
    Candidate = models.ForeignKey(Student, on_delete=models.CASCADE)


    def __str__(self):
        return self.AnswerSetNo








