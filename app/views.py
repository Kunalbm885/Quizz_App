from ast import And
from asyncio.windows_events import NULL
from email import message
from multiprocessing import context
import numbers
from turtle import up
from typing import Counter
from django.shortcuts import redirect, render
import os
import time
from app.models import AttemptedQuiz, Answer_Bank,QuizReport, Question, QuizInfo, Student, Teacher
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

import random

# Create your views here.


def Homepage(request):
    return render(request, "homepage.html")

#---------------------------------STUDENT--------------------------------------------------#

def TaketoSlogin(request):
    return render(request, "student/studentlogin.html")

def TaketoSregister(request ):
    return render(request, "student/studentregister.html")

def TaketoSdash(request,pk):
    c=QuizReport.objects.all().filter(Student=pk)
    return render(request, "student/studentdash.html" ,{'c':c})


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
            message = "Student Is Successfully Registered"
            return render(request, "student/studentregister.html", {'msg1': message})
        else:
            message = "Password does not match"
            return render(request, "student/studentregister.html", {'msg2': message})

studentname = ""
studentemail = ""

def StudentDash(request):
    global studentname
    global studentemail

    if request.method == "POST":
        smail = request.POST['smail']
        spassword = request.POST['spassword']
    try:
        student = Student.objects.get(studentemail=smail)
    except Student.DoesNotExist:
          message = "Student is Not Registered"
          return render(request, "student/studentlogin.html", {'msg': message})
    if student:
            if student.studentpass == spassword:
                request.session['stuname'] = student.studentname
                request.session['stuemail'] = student.studentemail
                studentemail=student.studentemail
            
                studentname = student.studentname


                c=QuizReport.objects.all().filter(Student=studentemail)
                print(c)
               

                return render(request, "student/studentdash.html",{'c':c})
            else:
                message = "Password is Incorrect"
                return render(request, "student/studentlogin.html", {'msg': message})
    elif student.studentpass is NULL and student.studentemail is NULL:
            message = "Student is Not Registered"
            return render(request, "student/studentlogin.html", {'msg': message})


# def SelectCourse(request):
#     global studentname
#     c = QuizInfo.objects.all()
#     s = AttemptedQuiz.objects.all().filter(sname = studentname,)
#     return render(request,"student/takecourse.html",{'c':c,'s':s})



# def SelectCourse(request):
#     c = QuizInfo.objects.all()
#     return render(request, "student/takecourse.html", {'c': c})


teacher=""
r=[]


def givexam(request, pk,eml ,time , name):
    
    global studentname,r
    te=Teacher.objects.get(teacheremail=name)
    name2=te.teachername
    time = QuizInfo.objects.get(teacherassigname=name2 , quizname=pk)
    date=time.Duedate
    time2 = time.Time
    timer=time.totaltime
    print(time2)
    print(timer)
    
    if request.method == 'POST':
    
        print(request.POST)
        # questions = Question.objects.all().filter(quiznameques=pk) 
        questions = r
        score=0
        tot=0
        wrong=0
        correct=0
        total=0
        Tm=0
        for q in questions:
            mks0 = q.marks
            tot+= mks0
            total+=1
           
            print()
            if q.answer ==  request.POST.get(q.question):
                mks = q.marks
                score+= mks
                correct+=1

                attemp = AttemptedQuiz.objects.create(tname=name,sname = studentname,isattempted = True,qname = pk)
                bnk = Answer_Bank.objects.create(
                  Student=eml,Question=q.question,Selected_Ans=q.answer,Quiz_Name=pk,Option1=q.option1,Option2=q.option2,Option3=q.option3,Option4=q.option4,answer=q.answer,marks=q.marks,Teacher=name)
            else:
                ans = request.POST.get(q.question)
                wrong+=1
                attemp = AttemptedQuiz.objects.create(tname=name,sname = studentname,isattempted = True,qname = pk)

                bnk = Answer_Bank.objects.create(
                  Student=eml,Question=q.question,Selected_Ans=ans,Quiz_Name=pk,Option1=q.option1,Option2=q.option2,Option3=q.option3,Option4=q.option4,answer=q.answer,marks=q.marks,Teacher=name)

        percent = score/(total*q.marks) *100
        percent = '{:.2f}'.format(percent)


       
        {'tot':tot}
        {'pk':pk}
        {'score':score}
        {'correct':correct}
        {'wrong':wrong}
        {'percent':percent}
        {'total':total}


     
        
        rep = QuizReport.objects.create(
                Student=eml, QuizName=pk, Score=score, Correct=correct , Incorrect=wrong , Total=total , Percentage = percent ,Total_Marks = tot,Teacher=name ,Date=date,Time=time2 ,TeacherName=name2)
        c=QuizReport.objects.all().filter(Student=eml)
       

        return render(request,'student/studentdash.html'  ,{'R':rep ,'c':c })

    
    else:

     print(name2)
        # for i in number:
    number=QuizInfo.objects.get(quizname=pk ,teacherassigname=name2  )
    numb= int(number.noofquest)
    questions = list(Question.objects.all().filter(quiznameques=pk,Teacher=name2))

    r = random.sample(questions,numb)  
    print(r) 
        
        # print(questions)
    return render(request,'student/givexam.html',{'questions': r ,'time':time ,'timer':timer})


    
       

        
 



def ToResultpage(request,eml):
    p = QuizReport.objects.all().filter(Student=eml)
    
    return render(request, "student/result.html",{'p':p })


def ToAnsPage(request,pk,eml ,tename):
    check2 = QuizReport.objects.all().filter(QuizName=pk,Student=eml,Teacher=tename)
    check = Answer_Bank.objects.all().filter(Quiz_Name=pk,Student=eml , Teacher=tename)
    

    print(check)
    print(check2)

    return render(request, "student/Correct.html",{'check': check,'pk':pk,'check2':check2})


def SelectCourse(request,pk):
    print(pk)
    global studentname
    c = QuizInfo.objects.all().filter(teacherassigname = pk)
    print(c)
    a=Teacher.objects.get(teachername=pk)
    pk2=a.teacheremail
    print(pk2)
    # a=QuizInfo.objects.get(teacherassigname = pk)
    # pk2=a.teacheremail
    s = AttemptedQuiz.objects.all().filter(tname=pk2)
    print(s)
    
    return render(request,"student/takecourse.html",{'c':c,'s':s ,'teachername':pk2 ,'pk':pk})



def SelectT(request):
    tnames = Teacher.objects.all()
    return render(request,"student/selteacher.html",{'teaname':tnames})



#---------------------------------TEACHER--------------------------------------------------#


def TaketoTlogin(request):
    return render(request, "teacher/teacherlogin.html")


def TaketoTreg(request):
    return render(request, "teacher/teacherregister.html")


def TeacherReg(request):
    tename = request.POST['tname']
    teemail = request.POST['temail']
    # tesub = request.POST['subject']

    tepass = request.POST['tpass']
    tecpass = request.POST['tcpass']

    user = Teacher.objects.filter(teacheremail=teemail)

    if user:
        message = "User is already Registered"
        return render(request, "teacher/teacherregister.html")
    else:
        if tepass == tecpass:
            newteacher = Teacher.objects.create(
                teachername=tename, teacheremail=teemail, teacherpass=tepass )
            message = "Teacher Is Successfully Registered !"
            return render(request, "teacher/teacherregister.html", {'msg1': message})
        else:
            message = "Password did not Matched !"



    return render(request, "teacher/teacherregister.html", {'msg2': message })


def TaketoTdash(request):
    global teachern

    c = QuizInfo.objects.all().filter(teacherassigname = teachern)

    return render(request, "teacher/teacherdash.html" , {'c':c})

teachern=""
def TeacherDash(request):
    global teachern
    if request.method == "POST":
        temail = request.POST['temail']
        tpassword = request.POST['tpass']
    try:
        teacher = Teacher.objects.get(teacheremail=temail)
    except Teacher.DoesNotExist:
         message = "Teacher is Not Registered"
         return render(request, "teacher/teacherlogin.html", {'msg': message})
    if teacher:
            if teacher.teacherpass == tpassword:
                request.session['tename'] = teacher.teachername
                teachern=teacher.teachername

                c = QuizInfo.objects.all().filter(teacherassigname = teachern)

                return render(request, "teacher/teacherdash.html",{'c':c})

           
            else:
                message = "Password is Incorrect"
                return render(request, "teacher/teacherlogin.html", {'msg': message})
    else:
            message = "Teacher is Not Registered"
            return render(request, "teacher/teacherregister.html", {'msg': message})


def TaketoMakequiz(request):
    return render(request, "teacher/makequiz.html")



quizn=""
def GetQuizInfo(request, pk):
    global quizn
    t = Teacher.objects.get(teachername=pk)
    taname = t.teachername
    quiznamee = request.POST['quizname']
    date = request.POST['date']
    time = request.POST['time']
    tottime = request.POST['tottime']
    noofquest = request.POST['no']


    newquizinfo = QuizInfo.objects.create(
        teacherassigname=taname, quizname=quiznamee, Duedate=date ,Time=time ,totaltime=tottime ,noofquest=noofquest)

    number=newquizinfo.noofquest
    print(number)
    q = QuizInfo.objects.get(quizname=quiznamee, teacherassigname=taname)
    request.session['quizn'] = q.quizname
    quizn=q.quizname
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
       Teacher=pk, quiznameques=qname, question=que, option1=opA, option2=opB, option3=opC, option4=opD, answer=ans, marks=mks)

    return render(request, "teacher/addquestions.html")




def GetPreview(request ,pk, fk):
    quiz=fk
    
    te=pk
    print(quiz)
    # print(te)
    total = 0
    show = Question.objects.all().filter(Teacher=pk,quiznameques=fk)
    # print(show)

    for s in show :
        mks = s.marks
        total += mks
    return render (request,"teacher/preview.html",{'show':show ,'total':total ,'name':quiz})



    

def EmailSending(request):
    global teachern,quizn
    template = render_to_string('teacher/demo1.html',{'quizname':quizn,'teachername':teachern})
    studente = Student.objects.values_list('studentemail',flat=True)
    for i in studente:
        email = EmailMessage(
            'New Quiz Assigned!',
            template,
            settings.EMAIL_HOST_USER,
            [i],
        )
        email.fail_silently = False
        email.send()

    message = "Quiz Assigned , Email Sent To Students !"


    return render(request,"teacher/makequiz.html",{'msg': message})




def quiz(request,pk):
    
    # global studentname
    c = QuizInfo.objects.all().filter(teacherassigname = pk)
    # s = AttemptedQuiz.objects.all().filter(sname = studentname)

   
    return render(request,"teacher/quiz.html",{'c':c})


student=""
em=""
def attempted(request,pk):
    global student
    global em
    global teachern
    print(student)
    print(pk)
    T = Teacher.objects.get(teachername=teachern)
    email = T.teacheremail
    print(email)

    stud = Student.objects.all()
    c = QuizReport.objects.all().filter(Teacher=email , QuizName=pk )
    print(c)
    print(stud)

    # for s in stud:
    #      print(s)
    #     #  print(c)
       

    #      for i in c:
    #          print(i)
    #          if  i.Student == s.studentemail  and i.QuizName == pk :
    #              print('Attempted')

    #          elif i.QuizName=="" and i.Student == s.studentemail:
    #              print('Not Attempted')
    #          elif i.QuizName=="" and i.Student == "":
    #              print('Not Attempted')
    #          else:
    #              print('none')

    return render(request,"teacher/attempted.html" ,{'s':stud ,'c':c ,'pk':pk})







def TakeToUD(request,pk,fk):
    u = QuizInfo.objects.get(teacherassigname=pk,quizname=fk)
    return render(request,"teacher/quiz.html",{'teaname':pk,'uquizname':fk,'u':u})

def UpdateQuizDetails(request,pk):
    p = pk
    print(pk)

    name = request.POST.get('quiz10','')
    print (name)
    update = QuizInfo.objects.get(teacherassigname=pk,quizname=name)
    
    update.noofquest = request.POST['no']
    update.totaltime = request.POST['tottime']
    update.Duedate = request.POST['date']
    update.Time = request.POST['time']

    update.save()

    return redirect('taketoquiz',pk=p)