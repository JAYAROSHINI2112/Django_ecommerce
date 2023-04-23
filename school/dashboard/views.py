from django.shortcuts import render
from classes . models import *
from teachers . models import *
from students . models import *
# Create your views here.
def dashboard(request):
    obj = classesregister.objects.all()
    return render(request,'dashboard.html',{'obj':obj})

def classdetails(request,id,cid):
    tech =  teachersregister.objects.filter(tclass = id)
    stu = studentsregister.objects.filter(sclass = id)
    var = classesregister.objects.get(cclass=cid)
    content = {'tech':tech,'stu':stu,'var':var}
    return render(request,'classdetails.html',content)