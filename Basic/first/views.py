from django.http import response,request
from django.shortcuts import render

# Create your views here.

def hai(request):
    return response.HttpResponse("<h1>Welcome to Zealous DJANGO training</h1>")

def hello(request):
    return response.HttpResponse("Enjoy Django")

def greet(request):
    return render(request,'hello.html')

def send(request):
    return render(request,'passing.html',{"just":"Hello Zealous!"})

def verify(request):
    if request.method=="POST":
        data1=request.POST['user']
        data2=request.POST['pass']
        if data1=="aarthi" and data2=="annakili":
            return render(request,'home.html',{"msg":"Logged successfully"})
        else:
            return render(request,'login.html',{"msg":"Login failed"})
    else:
        return render(request,'login.html',{"msg":"Login welcomes you"})