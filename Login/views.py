from Registration.models import Candidate
from django.shortcuts import render
from Registration.models import Candidate
from django.http.response import HttpResponse

# Create your views here.
def login(request):
    return render(request,"Login.html")

def loging(request):
    print("entering..................")
    email = request.POST.get('email')
    password = request.POST.get('password')
    accnttype = request.POST.get('accnttype')
    infolist=[]

    try:
        data = Candidate.objects.get(email=email, password = password, accnttype = accnttype) #select * from Candidate where email=email && password=password && accnttype=accnttype;

    except:
        return HttpResponse("Invalid Login Credentials")
    #print("entering again..................")
    #print(data.accnttype)
    request.session['log_email'] = email

    infolist.append(data.name)
    infolist.append(data.phone)
    infolist.append(data.email)
    infolist.append(data.dob)
    infolist.append(data.accnttype)
    
    if(data.accnttype=="teacher"):
        return render(request,"TeacherProfile.html",{ 'infolist':infolist })
        
    return render(request,"StudentProfile.html",{ 'infolist':infolist } )