from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'login.html')

def registations(request):
    return render(request,'registations.html')

