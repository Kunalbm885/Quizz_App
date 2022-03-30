from os import name
from django.urls import path,include
from django.views import View
from . import views
urlpatterns = [
    path("",views.Homepage,name="homepage"),

    #-------------------------------STUDENT--------------------------------------#
    path("taketoSlogin",views.TaketoSlogin,name="taketoSlogin"),
    path("taketoSreg",views.TaketoSregister,name="taketoSreg"),
    path("taketoSdash",views.TaketoSdash,name="taketoSdash"),
    path("studentregister",views.StudentReg,name="studentreg"),
    path("studentdash",views.StudentDash,name="studentdash"),
    path("selectcourse",views.SelectCourse,name="selectcourse"),
    path("taketogivexam <str:pk> <str:eml> ",views.givexam,name="taketogivexam"),
    path("taketoreportpage",views.ToResultpage,name="taketoreportpage"),




    #-------------------------------TEACHER--------------------------------------#
    path("taketoTlogin",views.TaketoTlogin,name="taketoTlogin"),
    path("teacherreg",views.TeacherReg,name="teacherreg"),
    path("taketoTreg",views.TaketoTreg,name="taketoTreg"),
    path("teacherdashboard",views.TeacherDash,name="teacherdash"),
    path("taketoTdash",views.TaketoTdash,name="taketoTdash"),
    path("makequiz",views.TaketoMakequiz,name="takemakequiz"),
    path("getquizinfo <str:pk>",views.GetQuizInfo,name="getquizinfo"),
    path("getquestion <str:pk> <str:fk>",views.GetQuestions,name="getquestions"),
]
