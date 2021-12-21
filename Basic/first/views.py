from django.http import response,request
from django.shortcuts import render

# Create your views here.

def hai(request):
    return response.HttpResponse("<h1>Welcome to Zealous DJANGO training</h1>")

def hello(request):
    return response.HttpResponse("Enjoy Django")