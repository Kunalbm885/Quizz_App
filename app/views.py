from email import message
from multiprocessing import context
import numbers
from typing import Counter
from django.shortcuts import redirect, render
import os
import time
from app.models import Answer_Bank,QuizReport, Question, QuizInfo, Student, Teacher
 

# Create your views here.


def Homepage(request):
    return render(request, "homepage.html")

#---------------------------------STUDENT--------------------------------------------------#


def TaketoSlogin(request):
    return render(request, "student/studentlogin.html")


def TaketoSregister(request):
    return render(request, "student/studentregister.html")


def TaketoSdash(request):
    return render(request, "student/studentdash.html")


def StudentReg(request):
    sname = request.POST['sname']
    semail = request.POST['semail']
    sroll = request.POST['rollno']
    spass = request.POST['spass']
    scpass = request.POST['scpass']

    user = Student.objects.filter(studentemail=semail)

    if user:
        message = "Student is already Registered"
        return render(request, "student/studentregister.html")
    else:
        if spass == scpass:
            newstudent = Student.objects.create(
                studentname=sname, studentemail=semail, studentrollno=sroll, studentpass=spass)
            message = "Student is successfull Registered"
            return render(request, "student/studentregister.html", {'msg': message})
        else:
            message = "Password does not match"
            return render(request, "student/studentregister.html", {'msg': message})



def StudentDash(request):
    if request.method == "POST":
        smail = request.POST['smail']
        spassword = request.POST['spassword']

        student = Student.objects.get(studentemail=smail)

        if student:
            if student.studentpass == spassword:
                request.session['stuname'] = student.studentname
                request.session['stuemail'] = student.studentemail

                return render(request, "student/studentdash.html")
            else:
                message = "Password is Incorrect"
                return render(request, "student/studentlogin.html", {'msg': message})
        else:
            message = "Student is Not Registered"
            return render(request, "student/studentlogin.html", {'msg': message})


def SelectCourse(request):
    c = QuizInfo.objects.all()
    return render(request, "student/takecourse.html", {'c': c})




def givexam(request, pk,eml):


    if request.method == 'POST':
    
        print(request.POST)
        questions = Question.objects.all().filter(quiznameques=pk) 
        score=0
        wrong=0
        correct=0
        total=0
        Tm=0
        for q in questions:
            total+=1
           
            print()
            
            
            if q.answer ==  request.POST.get(q.question):
                mks = q.marks
                score+= mks
                correct+=1
                bnk = Answer_Bank.objects.create(
                  Student=eml,Question=q.question,Selected_Ans=q.answer,Quiz_Name=pk)
            else:
                ans = request.POST.get(q.question)
                wrong+=1
                bnk = Answer_Bank.objects.create(
                  Student=eml,Question=q.question,Selected_Ans=ans,Quiz_Name=pk)

        percent = score/(total*q.marks) *100
        tmks = q.marks
        Tm+= tmks
        {'Tm':Tm}
        {'pk':pk}
        {'score':score}
        {'correct':correct}
        {'wrong':wrong}
        {'percent':percent}
        {'total':total}
        
        
        rep = QuizReport.objects.create(
                Student=eml, Quiz_Name=pk, Score=score, Correct=correct , Incorrect=wrong , Total=total , Percentage = percent )
    
        return render(request,'student/studentdash.html' ,{'R':rep})
    else:
    
        questions = Question.objects.all().filter(quiznameques=pk)
        return render(request,'student/givexam.html',{'questions': questions})



def ToResultpage(request):
    return render(request, "student/result.html")







#---------------------------------TEACHER--------------------------------------------------#


def TaketoTlogin(request):
    return render(request, "teacher/teacherlogin.html")


def TaketoTreg(request):
    return render(request, "teacher/teacherregister.html")


def TeacherReg(request):
    tename = request.POST['tname']
    teemail = request.POST['temail']
    tepass = request.POST['tpass']
    tecpass = request.POST['tcpass']

    user = Teacher.objects.filter(teacheremail=teemail)

    if user:
        message = "User is already Registered"
        return render(request, "teacher/teacherregister.html")
    else:
        if tepass == tecpass:
            newteacher = Teacher.objects.create(
                teachername=tename, teacheremail=teemail, teacherpass=tepass)
            message = "User is successfull Registered"
            return render(request, "teacher/teacherregister.html", {'msg': message})
        else:
            message = "Password does not match"
            return render(request, "teacher/teacherregister.html", {'msg': message})


def TaketoTdash(request):
    return render(request, "teacher/teacherdash.html")


def TeacherDash(request):
    if request.method == "POST":
        temail = request.POST['temail']
        tpassword = request.POST['tpass']

        teacher = Teacher.objects.get(teacheremail=temail)

        if teacher:
            if teacher.teacherpass == tpassword:
                request.session['tename'] = teacher.teachername
                return render(request, "teacher/teacherdash.html")
            else:
                message = "Password is Incorrect"
                return render(request, "teacher/teacherlogin.html", {'msg': message})
        else:
            message = "Teacher is Not Registered"
            return render(request, "teacher/teacherregister.html", {'msg': message})


def TaketoMakequiz(request):
    return render(request, "teacher/makequiz.html")


def GetQuizInfo(request, pk):
    t = Teacher.objects.get(teachername=pk)
    taname = t.teachername
    quiznamee = request.POST['quizname']
    date = request.POST['date']
    time = request.POST['time']
    newquizinfo = QuizInfo.objects.create(
        teacherassigname=taname, quizname=quiznamee, Duedate=date ,Time=time )
    q = QuizInfo.objects.get(quizname=quiznamee, teacherassigname=taname)
    request.session['quizn'] = q.quizname
    return render(request, "teacher/addquestions.html")


def GetQuestions(request, pk, fk):
    print(request.POST)
    

    q = QuizInfo.objects.get(teacherassigname=pk, quizname=fk)
    qname = q.quizname
    que = request.POST['question']
    opA =request.POST['optionA']
    opB =request.POST['optionB']
    opC =request.POST['optionC']
    opD =request.POST['optionD']
    ans =request.POST['ans']


    # ans = request.POST['ans']
    mks = request.POST['marks']
    
    

    newquestion = Question.objects.create(
        quiznameques=qname, question=que, option1=opA, option2=opB, option3=opC, option4=opD, answer=ans, marks=mks)

    return render(request, "teacher/addquestions.html")
