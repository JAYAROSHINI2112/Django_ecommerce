from django.shortcuts import render,redirect
from . models import *
from classes . models import *
# Create your views here.

def addteachers(request):
    clreg=classesregister.objects.all()
    if request.method == 'POST':
        sname=request.POST['name']
        sclass=request.POST['class']
        ssession=request.POST['session']
        obj=teachersregister.objects.create(tname=sname,tclass_id=sclass,tsession=ssession)
        obj.save()
        return redirect('viewteachers')
    else:
        data={'clreg':clreg}
        # print({'clreg':data})
    return render(request,'addteachers.html',data)

def viewteachers(request):
    obj=teachersregister.objects.filter(status=1).order_by('tclass')
    return render(request,'viewteachers.html',{'obj':obj})

def editteachers(request,id,cid):
    if request.method == 'POST':
        sname=request.POST['name']
        sclass=request.POST['class']
        ssession=request.POST['session']
        # print("1",sname,sclass,ssession)
        teachersregister.objects.filter(id=id).update(tname=sname,tclass=sclass,tsession=ssession)
        return redirect('viewteachers')
    else:
        clreg = classesregister.objects.get(id=cid)
        object = teachersregister.objects.get(id=id)
        iter = classesregister.objects.all()
        context = {'object': object, 'clreg': clreg,'iter':iter}
        # print(context)
        return render(request, 'editteachers.html', context)


def deleteteachers(request,id):
    teachersregister.objects.filter(id=id).update(status=0)
    return redirect('viewteachers')