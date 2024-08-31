from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

"""Location views"""
#location
def location(request):
    loc = Location.objects.all()
    return render(request,'location.html',{'loc': loc,})

#add location
def addlocation(request):
    if request.method == 'POST':
        locid = request.POST.get('locationid')
        locname = request.POST.get('locationname')
        locstatus = request.POST.get('status')

        loc = Location(location_code=locid,name=locname,location_status=locstatus)
        loc.save()
        return redirect('location')

#edit the location
def editlocation(request):
    loc = Location.objects.all()
    context = {'loc': loc,}
    return redirect(request,'location.html',context)

#update location in the table
def updatelocation(request,id):
    if request.method == 'POST':
        locid = request.POST.get('locationid')
        locname = request.POST.get('locationname')
        locstatus = request.POST.get('status')
        loc = Location(id=id,location_code=locid,name=locname,location_status=locstatus)
        loc.save()
        return redirect('location')

#delete location
def deletelocation(request,id):
    loc = Location.objects.filter(id=id).delete()
    return redirect('location')

"""Department views"""
#department
def department(request):
    dep = Department.objects.all()
    return render(request,'department.html',{'dep': dep,})

#add department
def adddepartment(request):
    if request.method == 'POST':
        depid = request.POST.get('departmentid')
        depname = request.POST.get('departmentname')
        depstatus = request.POST.get('status')

        dep = Department(department_code=depid,name=depname,department_status=depstatus)
        dep.save()
        return redirect('department')

#edit the department
def editdepartment(request):
    dep = Department.objects.all()
    context = {'dep': dep,}
    return redirect(request,'department.html',context)

#update department in the table
def updatedepartment(request,id):
    if request.method == 'POST':
        depid = request.POST.get('departmentid')
        depname = request.POST.get('departmentname')
        depstatus = request.POST.get('status')
        dep = Department(id=id,department_code=depid,name=depname,department_status=depstatus)
        dep.save()
        return redirect('department')

#delete department
def deletedepartment(request,id):
    dep = Department.objects.filter(id=id).delete()
    return redirect('department')

"""Designation views"""
#designation
def designation(request):
    des = Designation.objects.all()
    return render(request,'designation.html',{'des': des,})

#add designation
def adddesignation(request):
    if request.method == 'POST':
        desid = request.POST.get('designationid')
        desname = request.POST.get('designationname')
        desstatus = request.POST.get('status')
        des = Designation(designation_code=desid,name=desname,designation_status=desstatus)
        des.save()
        return redirect('designation')

#edit the designation
def editdesignation(request):
    des = Designation.objects.all()
    context = {'des': des,}
    return redirect(request,'designation.html',context)

#update designation in the table
def updatedesignation(request,id):
    if request.method == 'POST':
        desid = request.POST.get('designationid')
        desname = request.POST.get('designationname')
        desstatus = request.POST.get('status')
        des = Designation(id=id,designation_code=desid,name=desname,designation_status=desstatus)
        des.save()
        return redirect('designation')

#delete designation
def deletedesignation(request,id):
    des = Designation.objects.filter(id=id).delete()
    return redirect('designation')

"""level views"""
#level
def level(request):
    lvl = Level.objects.all()
    return render(request,'level.html',{'lvl': lvl,})

#add level
def addlevel(request):
    if request.method == 'POST':
        lvlid = request.POST.get('levelid')
        lvlname = request.POST.get('levelname')
        lvlstatus = request.POST.get('status')
        lvl = Level(level_code=lvlid,name=lvlname,level_status=lvlstatus)
        lvl.save()
        return redirect('level')

#edit the level
def editlevel(request):
    lvl = Level.objects.all()
    context = {'lvl': lvl,}
    return redirect(request,'level.html',context)

#update level in the table
def updatelevel(request,id):
    if request.method == 'POST':
        lvlid = request.POST.get('levelid')
        lvlname = request.POST.get('levelname')
        lvlstatus = request.POST.get('status')
        lvl = Level(id=id,level_code=lvlid,name=lvlname,level_status=lvlstatus)
        lvl.save()
        return redirect('level')

#delete level
def deletelevel(request,id):
    lvl = Level.objects.filter(id=id).delete()
    return redirect('level')

"""Employee views"""
#employee
def employee(request):
    emp = Employee.objects.all()
    loc = Location.objects.all()
    dep = Department.objects.all()
    des = Designation.objects.all()
    lvl = Level.objects.all()
    context = {'loc':loc,'dep':dep,'des':des,'lvl':lvl,'emp': emp}
    return render(request,'employee.html',context)

#add employee
def addemployee(request):
    if request.method == 'POST':
        empid = request.POST.get('employeeid')
        empfirstname = request.POST.get('firstname')
        empmiddlename = request.POST.get('middlename')
        emplastname = request.POST.get('lastname')
        empemail = request.POST.get('email2')
        empmobile = request.POST.get('mobilenumber')
        location_id = request.POST.get('emplocation')
        department_id = request.POST.get('empdepartment')
        designation_id = request.POST.get('empdesignation')
        level_id = request.POST.get('emplevel')
        empstatus = request.POST.get('status')
        # Retrieve the instance
        emplocation = Location.objects.get(id=location_id)
        empdepartment = Department.objects.get(id=department_id)
        empdesignation = Designation.objects.get(id=designation_id)
        emplevel = Level.objects.get(id=level_id)
        emp = Employee(user_code=empid,first_name=empfirstname,middle_name=empmiddlename,last_name=emplastname,email=empemail,mobile=empmobile,
                       location=emplocation,department=empdepartment,designation=empdesignation,level=emplevel,employee_status=empstatus)
        emp.save()
        return redirect('employee')

#edit the employee
def editemployee(request):
    emp = Employee.objects.all()
    loc = Location.objects.all()
    dep = Department.objects.all()
    des = Designation.objects.all()
    lvl = Level.objects.all()
    context = {'loc':loc,'dep':dep,'des':des,'lvl':lvl,'emp': emp}
    return render(request,'employee.html',context)

#update employee in the table
def updateemployee(request,id):
    if request.method == 'POST':
        empid = request.POST.get('employeeid')
        empfirstname = request.POST.get('firstname')
        empmiddlename = request.POST.get('middlename')
        emplastname = request.POST.get('lastname')
        empemail = request.POST.get('email2')
        empmobile = request.POST.get('mobilenumber')
        location_id = request.POST.get('emplocation')
        department_id = request.POST.get('empdepartment')
        designation_id = request.POST.get('empdesignation')
        level_id = request.POST.get('emplevel')
        empstatus = request.POST.get('status')
        # Retrieve the instance
        emplocation = Location.objects.get(id=location_id)
        empdepartment = Department.objects.get(id=department_id)
        empdesignation = Designation.objects.get(id=designation_id)
        emplevel = Level.objects.get(id=level_id)
        emp = Employee(id=id,user_code=empid,first_name=empfirstname,middle_name=empmiddlename,last_name=emplastname,email=empemail,mobile=empmobile,
                       location=emplocation,department=empdepartment,designation=empdesignation,level=emplevel,employee_status=empstatus)
        emp.save()
        return redirect('employee')

#delete employee
def deleteemployee(request,id):
    emp = Employee.objects.filter(id=id).delete()
    return redirect('employee')
