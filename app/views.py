from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topics inserted sucessfully')
    
    return render(request,'insert_topic.html')

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'topic':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
        WO.save()
        return HttpResponse('Webpage inserted sucessfully')
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    LOW=Webpage.objects.all()
    d={'webpage':LOW}
    if request.method=='POST':
        na=request.POST['na']
        au=request.POST['au']
        da=request.POST['da']

        WO=Webpage.objects.get_or_create(name=na)[0]
        WO.save()
    
        AO=Accessrecords.objects.get_or_create(name=WO,authour=au,date=da)[0]
        AO.save()
        return HttpResponse('Data Inserted Successfully ')

    return render(request,'insert_access.html',d)
    