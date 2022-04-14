from dataclasses import fields
from pyexpat import model
from django.db import models

# Create your models here.


class Teacher(models.Model):
    teachername = models.CharField(max_length=50)
    teacheremail = models.EmailField(max_length=30, primary_key=True)
    teacherpass = models.CharField(max_length=50)
    # Subject = models.CharField(default=1, max_length=50)

    def __str__(self):
        return self.teachername


class Student(models.Model):
    studentname = models.CharField(max_length=50)
    studentemail = models.EmailField(max_length=50, primary_key=True)
    studentrollno = models.BigIntegerField(20)
    studentpass = models.CharField(max_length=50)

    def __str__(self):
        return self.studentname


class QuizInfo(models.Model):
    teacherassigname = models.CharField(max_length=50)
    quizname = models.CharField(max_length=50)
    totaltime = models.CharField(default=1, max_length=50)
    noofquest = models.CharField(default=2, max_length=50)

    Duedate = models.CharField(default=1, max_length=50)
    Time = models.CharField(default=1, max_length=50)

    def __str__(self):
        return self.quizname


class Question(models.Model):
    Teacher = models.CharField(default=1, max_length=100)
    quiznameques = models.CharField(max_length=100)
    question = models.CharField(max_length=300)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    marks = models.BigIntegerField(default=1, max_length=3)

    def __str__(self):
        # fields ['quiznameques','question']
        return self.question


class QuizReport(models.Model):#konse teacher ka quiz diya voh daalde
    Student = models.CharField(max_length=100)
    Teacher=models.CharField(default=1,max_length=100)
    Date=models.CharField(default=1,max_length=100)
    Time=models.CharField(default=1,max_length=100)

    QuizName = models.CharField(max_length=300)

    Score = models.CharField(max_length=100)
    Total_Marks = models.CharField(default=10, max_length=100)

    Percentage = models.CharField(max_length=100)
    Correct = models.CharField(max_length=100)
    Incorrect = models.CharField(max_length=100)
    Total = models.CharField(max_length=100)

    def __str__(self):
        return self.QuizName


class Answer_Bank(models.Model):#konse teacher ka quiz diya voh daalde
    Student = models.CharField(max_length=100)
    Teacher=models.CharField(default=1,max_length=100)
    Quiz_Name = models.CharField(max_length=300)
    Question = models.CharField(default=1, max_length=300)
    Option1 = models.CharField(default=10, max_length=100)
    Option2 = models.CharField(default=10, max_length=100)
    Option3 = models.CharField(default=10, max_length=100)
    Option4 = models.CharField(default=10, max_length=100)
    answer = models.CharField(default=10, max_length=100)
    marks = models.BigIntegerField(default=1, max_length=3)
    Selected_Ans = models.CharField(default=1, max_length=300, null=True)

    def __str__(self):
        return self.Student


class AttemptedQuiz(models.Model):
    tname=models.CharField(default=1,max_length=100) #konse teacher ka quiz diya voh daalde
    sname = models.CharField(max_length=100)
    qname = models.CharField(max_length=50)
    isattempted = models.BooleanField(default=False)
