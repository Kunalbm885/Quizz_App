from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)


class QuizInfoAdmin(admin.ModelAdmin):
    list_display = ['teacherassigname', 'quizname' ,'Duedate']
admin.site.register(QuizInfo,QuizInfoAdmin )

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['quiznameques', 'question','answer','marks']
admin.site.register(Question,QuestionAdmin)


class QuizReportAdmin(admin.ModelAdmin):
    list_display = ['Student','Quiz_Name', 'Score','Correct','Total']
admin.site.register(QuizReport,QuizReportAdmin)


class Answer_BankAdmin(admin.ModelAdmin):
    list_display = ['Student', 'Quiz_Name','Question','Selected_Ans']
admin.site.register(Answer_Bank,Answer_BankAdmin)









