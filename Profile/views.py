#from django.db.models.fields import json
from django.http.response import HttpResponse
from django.shortcuts import render
import  json
from Profile.models import Tutorials,Exam
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def profile(request):

    return render(request,"Profile.html")

def tutorials(request):
    return render(request,"TeacherTutorials.html")

def studentTutorials(request):
    return render(request,"studentTutorials.html")

def exams(request):
    request.session['c'] = None
    print("---  c --- ",request.session['c'])
    return render(request,"exams.html")

@csrf_exempt
def uploadtutorial(request):
    data = json.loads(request.body)
    des = data['des']
    link = data['link']
    Tcode = "T"+data['Tcode']
    log_email = request.session['log_email']

    db = Tutorials(email=log_email,description=des,link=link,code=Tcode)
    db.save()
    return HttpResponse(" Your Tutorial Has been saved. ")

@csrf_exempt
def loadTeachersTutorial(request):
    print("........entering")
    log_email = request.session['log_email']  #suchismita@gmail.com
    datalist=[]
    data = Tutorials.objects.all().filter(email = log_email)  # select * from Tutorials where email = log_email
    print("........entering again")
    
    for i in range(len(data)):
        email = data[i].email
        description = data[i].description
        link = data[i].link
        code = data[i].code
        value = { 'email': email, 'description': description, 'link':link, 'code':code }
        datalist.append(value)
    
    return JsonResponse({'data':datalist})

def getTeachersTutorial(request):
    print("........entering")
    #log_email = request.session['log_email']  
    datalist=[]
    data = Tutorials.objects.all()  # select * from Tutorials where email = log_email
    print("........entering again")
        
    for i in range(len(data)):
        email = data[i].email
        description = data[i].description
        link = data[i].link
        code = data[i].code
        value = { 'email': email, 'description': description, 'link':link, 'code':code }
        datalist.append(value)
    
    return JsonResponse({'data':datalist})

@csrf_exempt
def uploadExam(request):
    obj = json.loads(request.body)
    email = request.session['log_email']
    questions = obj['questions']
    options_a = obj['options_a']
    options_b = obj['options_b']
    options_c = obj['options_c']
    options_d = obj['options_d']
    answers = obj['answers']
    Ecode = obj['Ecode']
    for i in range(5):
        data = Exam(email = email, questions = questions[i], options_a = options_a[i], options_b = options_b[i], options_c = options_c[i], options_d = options_d[i], answers = answers[i], ecode = Ecode )
        data.save() 
        
    return HttpResponse(" Exam Uploaded Successfully. Please Refresh. ")

def give_exams(request):
    conductedByList = []
    EcodeList = []
    info = []

    Ecode = Exam.objects.all().values('ecode').distinct()
    #print( Ecode.ecode )
    for i in Ecode:
        EcodeList.append(i['ecode'])
    
    
    if( len( EcodeList )>0 ):
        return render(request,"examList.html", {'EcodeList':EcodeList} )
    
    return HttpResponse(" No Exams To Show ")

@csrf_exempt
def attemptExam(request):
    print("............................................",request.body)
    data = json.loads(request.body)
    ecode = data['ecode']
    request.session['ecode'] = ecode
    exam = Exam.objects.all().filter(ecode = ecode)
    print(" exam = ",exam)
    examList = []
    
    for i in range( len(exam) ):
        obj = { 'questions':exam[i].questions, 'options_a':exam[i].options_a, 'options_b':exam[i].options_b, 'options_c':exam[i].options_c, 'options_d':exam[i].options_d }
        examList.append(obj)
    
    return JsonResponse( { 'examList':examList } )

def submitTest(request):
    answer1 = ""
    answer2 = ""
    answer3 = ""
    answer4 = ""
    answer5 = ""
    score = 0

    ecode = request.session['ecode']
    data = Exam.objects.all().filter(ecode=ecode)
    print(data[0].ecode)
    
    answer1 = answer1+(request.POST.get('question1'))
    answer2 = answer2+(request.POST.get('question2'))
    answer3 = answer3+(request.POST.get('question3'))
    answer4 = answer4+(request.POST.get('question4'))
    answer5 = answer5+(request.POST.get('question5'))
    answerList=[]

    answerList.append(answer1)
    answerList.append(answer2)
    answerList.append(answer3)
    answerList.append(answer4)
    answerList.append(answer5)

    for i in range(5):
        print(answerList[i],"..............",data[i].answers)
    
    for i in range(5):
        if( answerList[i]==data[i].answers):
            score=score+1
    
    return HttpResponse( "Your Test Score = "+str(score) )

@csrf_exempt
def deleteTutorial(request):
    tcode = ( json.loads(request.body) )['ecode']
    Tutorials.objects.all().filter( code = tcode ).delete()
    return HttpResponse("Tutorial deleted . Please refresh")

@csrf_exempt
def deleteExam(request):
    ecode = ( json.loads(request.body) )['ecode']
    try:
        Exam.objects.all().filter(ecode = ecode).delete()
        return HttpResponse("Exam Deleted . Please Refresh")
    except:
        return HttpResponse("Invalid E-Code")
    