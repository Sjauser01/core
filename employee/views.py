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

"""classification views"""
#classification
def classification(request):
    cls = Classification.objects.all()
    return render(request,'classification.html',{'cls': cls,})

#add classification
def addclassification(request):
    if request.method == 'POST':
        clsid = request.POST.get('classificationid')
        clsname = request.POST.get('classificationname')
        clsstatus = request.POST.get('status')
        cls = Classification(classification_code=clsid,name=clsname,classification_status=clsstatus)
        cls.save()
        return redirect('classification')

#edit the classification
def editclassification(request):
    cls = Classification.objects.all()
    context = {'cls': cls,}
    return redirect(request,'classification.html',context)

#update classification in the table
def updateclassification(request,id):
    if request.method == 'POST':
        clsid = request.POST.get('classificationid')
        clsname = request.POST.get('classificationname')
        clsstatus = request.POST.get('status')
        cls = Classification(id=id,classification_code=clsid,name=clsname,classification_status=clsstatus)
        cls.save()
        return redirect('classification')

#delete classification
def deleteclassification(request,id):
    cls = Classification.objects.filter(id=id).delete()
    return redirect('classification')

"""suffix views"""
#suffix
def suffix(request):
    sfx = Suffix.objects.all()
    return render(request,'suffix.html',{'sfx': sfx,})

#add suffix
def addsuffix(request):
    if request.method == 'POST':
        sfxid = request.POST.get('suffixid')
        sfxname = request.POST.get('suffixname')
        sfxstatus = request.POST.get('status')
        sfx = Suffix(suffix_code=sfxid,name=sfxname,suffix_status=sfxstatus)
        sfx.save()
        return redirect('suffix')

#edit the suffix
def editsuffix(request):
    sfx = Suffix.objects.all()
    context = {'sfx': sfx,}
    return redirect(request,'suffix.html',context)

#update suffix in the table
def updatesuffix(request,id):
    if request.method == 'POST':
        sfxid = request.POST.get('suffixid')
        sfxname = request.POST.get('suffixname')
        sfxstatus = request.POST.get('status')
        sfx = Suffix(id=id,suffix_code=sfxid,name=sfxname,suffix_status=sfxstatus)
        sfx.save()
        return redirect('suffix')

#delete suffix
def deletesuffix(request,id):
    sfx = Suffix.objects.filter(id=id).delete()
    return redirect('suffix')

"""prefix views"""
#prefix
def prefix(request):
    prx = Prefix.objects.all()
    return render(request,'prefix.html',{'prx': prx,})

#add prefix
def addprefix(request):
    if request.method == 'POST':
        prxid = request.POST.get('prefixid')
        prxname = request.POST.get('prefixname')
        prxstatus = request.POST.get('status')
        prx = Prefix(prefix_code=prxid,name=prxname,prefix_status=prxstatus)
        prx.save()
        return redirect('prefix')

#edit the prefix
def editprefix(request):
    prx = Prefix.objects.all()
    context = {'prx': prx,}
    return redirect(request,'prefix.html',context)

#update prefix in the table
def updateprefix(request,id):
    if request.method == 'POST':
        prxid = request.POST.get('prefixid')
        prxname = request.POST.get('prefixname')
        prxstatus = request.POST.get('status')
        prx = Prefix(id=id,prefix_code=prxid,name=prxname,prefix_status=prxstatus)
        prx.save()
        return redirect('prefix')

#delete prefix
def deleteprefix(request,id):
    prx = Prefix.objects.filter(id=id).delete()
    return redirect('prefix')

"""Pre setup views"""
#setup
def setup(request):
    return render(request,'setup.html')

def addsetup(request):
    if request.method == 'POST':
        return redirect('setup')

@csrf_exempt
def save_form_data(request):
    if request.method == 'POST':
        # Save Series data (Page 1)
        series_data = Series(
            field1=request.POST.get('mainOption1', ''),
            field2=request.POST.get('mainOption2', ''),
            # Add fields up to field15
            field15=request.POST.get('mainOption15', '')
        )
        series_data.save()

        # Save CompAndBOM data (Page 2)
        comp_and_bom_data = CompAndBOM(
            choice1=request.POST.get('choice1', ''),
            choice2=request.POST.get('choice2', ''),
            choice3=request.POST.get('choice3', ''),
            choice4=request.POST.get('choice4', '')
        )
        comp_and_bom_data.save()

        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)

"""plant views"""
#plant
def plant(request):
    plt = Plant.objects.all()
    loc = Location.objects.all()
    context = {'loc':loc,'plt': plt}
    return render(request,'plant.html',context)

#add plant
def addplant(request):
    if request.method == 'POST':
        pltid = request.POST.get('plantid')
        pltname = request.POST.get('plantname')
        pltloc_id = request.POST.get('plantlocation')
        pltstatus = request.POST.get('status')

        # Retrieve all locations for the dropdown
        loc = Location.objects.all()

        # Check if a plant with the same plant_code already exists
        if Plant.objects.filter(plant_code=pltid).exists():
            # Issue a warning message and render the form again with the modal open
            messages.warning(request, f"Plant Code '{pltid}' already exists. Please choose a different Plant Code.")
            return render(request, 'plant.html', {'loc': loc, 'show_modal': True})

        # Retrieve the selected location instance
        try:
            pltlocation = Location.objects.get(id=pltloc_id)
        except Location.DoesNotExist:
            messages.error(request, "Selected location does not exist.")
            return render(request, 'plant.html', {'loc': loc, 'show_modal': True})

        # Create and save the new plant if no duplicate plant_code is found
        plt = Plant(plant_code=pltid, name=pltname, location=pltlocation, plant_status=pltstatus)
        plt.save()

        # Issue a success message and redirect back to the plant list
        messages.success(request, "Plant added successfully!")
        return redirect('plant')

    # If the request method is GET, render the form with location options
    loc = Location.objects.all()  # Pass locations to the template
    return render(request, 'plant.html', {'loc': loc})
#edit the plant
def editplant(request):
    plt = Plant.objects.all()
    loc = Location.objects.all()
    context = {'plt': plt,'loc':loc}
    return render(request,'plant.html',context)

#update plant in the table
def updateplant(request,id):
    if request.method == 'POST':
        pltid = request.POST.get('plantid')
        pltname = request.POST.get('plantname')
        pltloc_id = request.POST.get('plantlocation')
        pltstatus = request.POST.get('status')
        # Retrieve the instance
        pltlocation = Location.objects.get(id=pltloc_id)
        plt = Plant(id=id,plant_code=pltid,name=pltname,location=pltlocation,plant_status=pltstatus)
        plt.save()
        return redirect('plant')

#delete plant
def deleteplant(request,id):
    plt = Plant.objects.filter(id=id).delete()
    return redirect('plant')

"""Storage views"""
#storage
def storage(request):
    stl = Storage.objects.all()
    plt = Plant.objects.all()
    context = {'plt':plt,'stl': stl}
    return render(request,'storage.html',context)

#add storage
def addstorage(request):
    if request.method == 'POST':
        stlid = request.POST.get('storageid')
        stlname = request.POST.get('storagename')
        stlplant_id = request.POST.get('storageplant')
        stltype = request.POST.get('storagetype')
        stldimension = request.POST.get('storagedimension')
        # Retrieve the instance
        stlplant = Plant.objects.get(id=stlplant_id)
        stl = Storage(storage_code=stlid,description=stlname,plant=stlplant,storage_type=stltype,dimension=stldimension)
        stl.save()
        return redirect('storage')

#edit the storage
def editstorage(request):
    stl = Storage.objects.all()
    plt = plant.objects.all()
    context = {'stl': stl,'plt':plt}
    return render(request,'storage.html',context)

#update storage in the table
def updatestorage(request,id):
    if request.method == 'POST':
        stlid = request.POST.get('storageid')
        stlname = request.POST.get('storagename')
        stlplant_id = request.POST.get('storageplant')
        stltype = request.POST.get('storagetype')
        stldimension = request.POST.get('storagedimension')
        # Retrieve the instance
        stlplant = Plant.objects.get(id=stlplant_id)
        stl = Storage(id=id,storage_code=stlid,description=stlname,plant=stlplant,storage_type=stltype,dimension=stldimension)
        stl.save()
        return redirect('storage')

#delete storage
def deletestorage(request,id):
    stl = Storage.objects.filter(id=id).delete()
    return redirect('storage')
