from django.shortcuts import render
# from django.http import HttpResponse
from app.models import *
# Create your views here.

'''
def Insert_Topic(request):
    tn = input('Enter the Topic Name : ')
    to = Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('Data is Inserted')

def Insert_Webpage(request):
    tn = input('Enter the Movie name and link :')
    to= Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n = input('Enter name of actor : ')
    u = input('movie url :')
    wo = Webpage.objects.get_or_create(topic_name=to,name=n,url=u)
    wo.save()
    return HttpResponse('! data inserted')

def Insert_Ac(request):
    tn = input('Enter the Movie name and link :')
    to= Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n = input('Enter name of actor : ')
    u = input('movie url :')
    wo = Webpage.objects.get_or_create(topic_name=to,name=n,url=u)
    wo.save()
    d = input('enter Date :')
    return HttpResponse('! data inserted')

    '''

def display_topics(request):
    
    QSTO=Topic.objects.all()

    d = {'QSTO':QSTO}

    return render(request,'display_topics.html',d)

def insert_topics(request):
    to = input('enter the Tpoic name :')

    To =Topic.objects.get(topic_name=to)
    To.save()
    QSTO=Topic.objects.all()


    d = {'QSTO':QSTO}

    return render(request,'display_topics.html',d)



def display_Webpage(request):
    
    QSWO = Webpage.objects.all()

    QSWO = Webpage.objects.all().order_by('name')
    QSWO = Webpage.objects.filter().order_by('-name')
    QSWO = Webpage.objects.exclude()
    QSWO = Webpage.objects.filter(name=3)

    QSWO = Webpage.objects.all()


    d = {'QSWO':QSWO}
    
    return render(request,'display_Webpage.html',d)

def insert_webpage(request):

    wo = input('Enter the Topic name :')
    na = input('Enter the name :')
    ur = input('enter the url')

    TO = Topic.objects.get(topic_name=wo)
    TO.save()

    WO = Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
    WO.save()

    QSWO = Webpage.objects.all()

    d = {'QSWO':QSWO}
    
    return render(request,'display_Webpage.html',d)

def display_AccessRecord(request):

    QSARO = AccessRecord.objects.all()

    d= {'QSARO' : QSARO}
    
    return render (request,'display_AccessRecord.html',d)

def insert_AccessRecord(request):
    pk=input('Enter the pk:')
    wo=input('Enter the name :')
    dt=input('Enter the date :')
    auth=input('Enter the author :')
    e=input('Enter the Email :')

    wo = Webpage.objects.get(pk=pk)
    wo.save()

    ao = AccessRecord.objects.get_or_create(name=wo,date=dt,author=auth,email=e)[0]
    ao.save()

    QSARO = AccessRecord.objects.all()

    d= {'QSARO' : QSARO}
    
    return render (request,'display_AccessRecord.html',d)
