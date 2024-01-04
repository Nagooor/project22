from django.shortcuts import render

#Create your views here.
from app.models import *
from django.http import HttpResponse
def display_dept(request):
    QLDO=Department.objects.all()
    d={'Department':QLDO}
    return render(request,'display_dept.html',d)

def display_emp(request):
    QLEO=Employee.objects.all()
    d={'Employee':QLEO}
    return render(request,'display_emp.html',d)

def display_salgrade(request):
    QLSO=Salgrade.objects.all()
    d={'Salgrade':QLSO}
    return render(request,'display_salgrade.html',d)

def display_bonus(request):
    QLBO=Bonus.objects.all()
    d={'Bonus':QLBO}
    return render(request,'display_bonus.html',d)



def insert_dept(request):
    dno=int(input('enter a deptno'))
    dna=input('enter a deptname')
    lo=input('enter a location')
    DTO=Department.objects.get_or_create(deptno=dno,dname=dna,loc=lo)[0]
    DTO.save()
    return HttpResponse('dept is created')

def insert_emp(request):
    dno=int(input('enter a deptno'))
    eno=int(input('enter a empno'))
    ena=input('enter a empyee name')
    jo=input('enter a job')
    mgr=input('enter a mgr')
    hd=input('enter a date')
    sal=int(input('enter a sal'))
    com=int(input('enter a comm'))
    TO=Department.objects.get(deptno=dno)
    NEO=Employee.objects.get_or_create(deptno=TO,empno=eno,ename=ena,job=jo,mgr=mgr,hiredate=hd,sal=sal,comm=com)[0]
    NEO.save()
    return HttpResponse('emp is created')

def insert_salgrade(request):
    gr=int(input('enter a grade'))
    ls=int(input('enter a losal'))
    hs=int(input('enter a hisal'))
    SO=Employee.objects.get(grade=gr)
    SGO=Salgrade.objects.get_or_create(grade=SO,losal=ls,hisal=hs)[0]
    SGO.save()
    return HttpResponse('salgrade is created')

def insert_bonus(request):
    a=int(input('enter a amount'))
    ATO=Bonus.objects.get_or_create(amount=a)[0]
    ATO.save()
    return HttpResponse('bonus table is created')

