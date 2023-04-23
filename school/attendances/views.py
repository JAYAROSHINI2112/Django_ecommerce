from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from classes . models import *
from students . models import *
from . models import *

def attendanceclass(request):
    obj = classesregister.objects.all()
    print('obj',obj)
    return render(request,'attendanceclass.html',{'obj':obj})

def viewattendanceclass(request,id):
    obj = attendclassmaster.objects.filter(classid=id).order_by('-data')
    var = classesregister.objects.get(id=id)
    content = {'id':id,'obj':obj,'var':var}
    return render(request,'viewattendanceclass.html',content) 

def addattendance(request,id):
    content = {'id':id}
    if request.method == 'POST':
        classname = request.POST['class']
        date = request.POST['date']
        classid = request.POST['cid']
        obj=attendclassmaster.objects.create(classname=classname,classid=classid,data=date)
        obj.save()
        return redirect('viewattendanceclass',id)
        
    else: 
        obj = classesregister.objects.get(id=id)
        return render(request,'addattendancedate.html',{'obj':obj})
    
    
def attendanceentry(request,cid,did):
    clas = classesregister.objects.get(id=cid)
    date = attendclassmaster.objects.get(id=did)
    studs = studentsregister.objects.filter(sclass_id=cid)
    content = {'clas':clas,'date':date,'studs':studs}
    return render(request,'attendanceentry.html',content)