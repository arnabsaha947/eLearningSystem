"""eLearningSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path
from Home import views as hbv
from Registration import views as rv
from Login import views as lv
from Profile import views as pv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hbv.Homebase,name="homeBase"),
    path('registration',rv.registration,name="registration"),
    path('login',lv.login,name="login"),
    path('contacts',hbv.contact,name="contacts"),
    path('about',hbv.about,name="about"),
    path('registered',rv.registered,name="registered"),
    path('loging',lv.loging,name="loging"),    
    path('tutorials',pv.tutorials,name="tutorials"),
    path('studentTutorials',pv.studentTutorials,name="studentTutorials"),
    path('exams',pv.exams,name="exams"),
    path('uploadtutorial',pv.uploadtutorial,name="uploadtutorial"),
    path('loadTeachersTutorial',pv.loadTeachersTutorial,name="loadTeachersTutorial"),
    path('getTeachersTutorial',pv.getTeachersTutorial,name="getTeachersTutorial"),
    path('uploadExam',pv.uploadExam,name="uploadExam"),
    path('give_exams',pv.give_exams,name="give_exams"),
    path('attemptExam',pv.attemptExam,name="attemptExam"),
    path('submitTest',pv.submitTest,name="submitTest"),
    path('deleteTutorial',pv.deleteTutorial,name="deleteTutorial"),
    path('deleteExam',pv.deleteExam,name="deleteExam"),
    
]
