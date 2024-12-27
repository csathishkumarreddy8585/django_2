from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    tn=input('enter the topicname:-')
    TOD=Topic.objects.get_or_create(topic_name=tn)
    if TOD[1]:
        return HttpResponse('data is inserted')
    else:
       return HttpResponse('data  is already present')

def insert_webpage(request):
    tn=input('enter the topicname:-')
    name=input('enter the name:-')
    url=input('enter the url:-')
    email=input('enter the email:-')

    LTO=Topic.objects.filter(topic_name=tn) #list  of topic object
    if LTO:
        WDO=Web_page.objects.get_or_create(topic_name=LTO[0],name=name,url=url,email=email)#webpage data object
        if WDO[1]:
            return HttpResponse('data is inserted')
        else:
            return HttpResponse('data  is already present')
    else:
            return HttpResponse('topic  is already  not present')

def insert_accessrecord(request):
    
    pk=int(input('enter the webid:-'))
    author=input('enter the author:-')
    date=input('enter the date:-')

    LWO=Web_page.objects.filter(id=pk) #list  of webpage object
    if LWO:
        ADO=Access_Record.objects.get_or_create(name=LWO[0],author=author,date=date)#access record data object
        if ADO[1]:
            return HttpResponse('data is inserted')
        else:
            return HttpResponse('data  is already present')
    else:
            return HttpResponse('topic  is already  not present')
            