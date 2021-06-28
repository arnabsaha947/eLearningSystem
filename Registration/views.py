from django.http.response import HttpResponse
from django.shortcuts import render
from Registration.models import Candidate

# Create your views here.
def registration(request):
    return render(request,"Registration.html")


def registered(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    wyd = request.POST.get('wyd')
    dob = request.POST.get('dob')
    accnttype = request.POST.get('accnttype')
    password = request.POST.get('password')
    if( name=="" or phone=="" or email=="" or wyd=="" or dob=="" or accnttype=="" or password=="" ):
        return HttpResponse("Please Fill All Info Correctly")

    try:
        data = Candidate(name=name, phone=phone, email=email,wyd=wyd,dob=dob, accnttype=accnttype, password=password)
        data.save()
        return render(request,"blank.html")
    except:
        return HttpResponse("Account Already Exists")
    

    


