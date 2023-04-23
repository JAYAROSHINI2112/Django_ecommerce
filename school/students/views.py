from django.shortcuts import render,redirect
from . models import *
from classes . models import *
# Create your views here.

def addstudents(request):
    clreg=classesregister.objects.all()
    if request.method == 'POST':
        sname=request.POST['name']
        sclass=request.POST['class']
        ssession=request.POST['session']
        obj=studentsregister.objects.create(sname=sname,sclass_id=sclass,ssession=ssession)
        obj.save()
        return redirect('viewstudents')
    else:
        data={'clreg':clreg}
        # print({'clreg':data})
    return render(request,'addstudents.html',data)

def viewstudents(request):
    obj=studentsregister.objects.filter(status=1).order_by('sclass_id')
    return render(request,'viewstudents.html',{'obj':obj})

def editstudents(request,id,cid):
    if request.method == 'POST':
        sname=request.POST['name']
        sclass=request.POST['class']
        ssession=request.POST['session']
        studentsregister.objects.filter(id=id).update(sname=sname,sclass=sclass,ssession=ssession)
        return redirect('viewstudents')
    else:
        clreg = classesregister.objects.get(id=cid)
        object = studentsregister.objects.get(id=id)
        iter = classesregister.objects.all()
        context = {'object': object, 'clreg': clreg,'iter':iter}
        return render(request,'editstudents.html', context)

def deletestudents(request,id):
    studentsregister.objects.filter(id=id).update(status=0)
    return redirect('viewstudents')