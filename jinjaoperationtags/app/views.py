from django.shortcuts import render

# Create your views here.




def conditions(request):
    d={'name':'sathish','age':22 }
    return render(request,'conditions.html',d)
    
