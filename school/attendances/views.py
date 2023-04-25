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
 
 
def deleteattendanceclass(request,did,id):
        attendclassmaster.objects.filter(id=id).delete()
        return redirect('viewattendanceclass',did)

    
def attendanceentrys(request,cid,did):
    if request.method == "POST":
        studs = studentsregister.objects.filter(sclass_id=cid)
        objcount = request.POST['objcount']   
        print('objcount',objcount)
        for j in studs:
            sid =  request.POST.get(f'sid{j.id}')
            cid = request.POST.get(f'cid{j.id}')
            did = request.POST.get(f'did{j.id}')
            pid = request.POST.get(f'val{j.id}')
            uid = request.POST.get(f'uid{j.id}')
            # print(j,"--",sid,cid,did,pid,objcount)
            # attendanceentry.objects.create(studid=sid,classid=cid,dateid=did,pafield=pid)
            if objcount == '0':
                attendanceentry.objects.create(studid=sid,classid=cid,dateid=did,pafield=pid)
            else:
                print(j,"--",sid,cid,did,pid,objcount,uid)
                attendanceentry.objects.filter(id=uid).update(studid=sid,classid=cid,dateid=did,pafield=pid)
            # attendanceentry.objects.create(studid=request.POST.get(f'sid{j.id}'),classid=request.POST.get(f'cid{j.id}'),dateid=request.POST.get(f'did{j.id}'),pafield=request.POST.get(f'val{j.id}'))
            # print(j.id,"--",pid)
        return redirect('viewattendanceclass',cid)
   
    else:     
        clas = classesregister.objects.get(id=cid)
        date = attendclassmaster.objects.get(id=did)
        studs = studentsregister.objects.filter(sclass_id=cid)
        obj = attendanceentry.objects.filter(classid=cid).filter(dateid=did)
        object = attendanceentry.objects.filter(classid=cid).filter(dateid=did)
        sfield = selectfield.objects.all()
        print('obj',obj)
        content = {'clas':clas,'date':date,'studs':studs,'obj':obj.count(),'object':object,'sfield':sfield}
        # print('clas',clas,'date',date,'studs',studs)
        return render(request,'attendanceentry.html',content)