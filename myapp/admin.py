from django.contrib import admin
from .models import Student, Teacher, QuizSet, Question, AnswerSet
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(QuizSet)
admin.site.register(Question)
admin.site.register(AnswerSet)

