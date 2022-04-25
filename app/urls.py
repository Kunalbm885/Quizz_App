from os import name
from django.urls import path,include
from django.views import View
from . import views
urlpatterns = [
    path("",views.Homepage,name="homepage"),

    #-------------------------------STUDENT--------------------------------------#
    path("taketoSlogin",views.TaketoSlogin,name="taketoSlogin"),
    path("taketoSreg",views.TaketoSregister,name="taketoSreg"),
    path("taketoSdash  <str:pk>",views.TaketoSdash,name="taketoSdash"),
    path("studentregister",views.StudentReg,name="studentreg"),
    path("studentdash",views.StudentDash,name="studentdash"),
    # path("selectcourse",views.SelectCourse,name="selectcourse"),
    path("taketogivexam <str:pk> <str:eml> <str:time> <str:name>",views.givexam,name="taketogivexam"),
    path("taketoreportpage <str:eml>",views.ToResultpage,name="taketoreportpage"),
    path("correctansdisp <str:pk> <str:eml> <str:tename>",views.ToAnsPage,name="correctansdisp"),
    path("selectcourse <str:pk>",views.SelectCourse,name="selectcourse"),
    path("selectteacher",views.SelectT,name="selectT"),




    #-------------------------------TEACHER--------------------------------------#
    path("taketoTlogin",views.TaketoTlogin,name="taketoTlogin"),
    path("teacherreg",views.TeacherReg,name="teacherreg"),
    path("taketoTreg",views.TaketoTreg,name="taketoTreg"),
    path("teacherdashboard",views.TeacherDash,name="teacherdash"),
    path("taketoTdash",views.TaketoTdash,name="taketoTdash"),
    path("makequiz",views.TaketoMakequiz,name="takemakequiz"),
    path("getquizinfo <str:pk>",views.GetQuizInfo,name="getquizinfo"),
    path("getquestion <str:pk> <str:fk>",views.GetQuestions,name="getquestions"),
    path("taketoPreview <str:pk> <str:fk>",views.GetPreview,name="taketoPreview"),
    path("emailsend",views.EmailSending,name="emailsend"),
    path("taketoquiz <str:pk>  ",views.quiz,name="taketoquiz"),

    path("taketoattempted <str:pk>",views.attempted,name="taketoattempted"),
    path("taktoUpdateDue <str:pk> <str:fk>",views.TakeToUD,name="taketoUD"),
<<<<<<< HEAD
    path("UpdateDetails <str:pk> <str:fk>",views.UpdateQuizDetails,name="updatedetails"),
=======
    path("UpdateDetails <str:pk> ",views.UpdateQuizDetails,name="updatedetails"),




>>>>>>> e49db1a96a23fb1884c1512f9e1e48de9f69bd2e
]
