from django.shortcuts import render,redirect,HttpResponseRedirect
from . models import *
# Create your views here.

def addclasses(request):
    if request.method == 'POST':
        sclass=request.POST['class']
        obj=classesregister.objects.create(cclass=sclass)
        obj.save()
        return HttpResponseRedirect('viewclasses')
    return render(request,'addclasses.html')

def viewclasses(request):
    obj=classesregister.objects.all()
    return render(request,'viewclasses.html',{'obj':obj})

def editclasses(request,id):
      if request.method == 'POST':
        sclass=request.POST['class']
        classesregister.objects.filter(id=id).update(cclass=sclass)
        return redirect('viewclasses')
      else:
        object=classesregister.objects.get(id=id)
        return render(request,'editclasses.html',{'object':object})

def deleteclasses(request,id):
    classesregister.objects.filter(id=id).delete()
    obj=classesregister.objects.all()
    return render(request,'viewclasses.html',{'obj':obj})