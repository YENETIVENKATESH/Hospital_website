from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def page1(request):
    if request.method=="GET":
        return render(request,"hospital/page1.html")

    elif request.method== "POST":
        print(request.POST)
        name ={"patient":request.POST['NAME'], "date":request.POST['date'], "time":request.POST["time"]}
        return render(request,"hospital/detail.html",name)


def about(request):
    return render(request,"hospital/about.html")

def contact(request):
    return render(request,"hospital/contact.html")

def doctor(request):
    return render(request,"hospital/doctor.html")



