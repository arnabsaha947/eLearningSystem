from django.shortcuts import render

# Create your views here.
def Homebase(request):
    return render(request,"Homebase.html")

def contact(request):
    return render(request,"Contact.html")

def about(request):
    return render(request,"About.html")