from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name="home"),

    path('location/',views.location, name="location"),
    path('addlocation/',views.addlocation, name="addlocation"),
    path('editlocation/',views.editlocation, name="editlocation"),
    path('updatelocation/<str:id>',views.updatelocation, name="updatelocation"),
    path('deletelocation/<str:id>',views.deletelocation, name="deletelocation"),
    
    path('department/',views.department, name="department"),
    path('adddepartment/',views.adddepartment, name="adddepartment"),
    path('editdepartment/',views.editdepartment, name="editdepartment"),
    path('updatedepartment/<str:id>',views.updatedepartment, name="updatedepartment"),
    path('deletedepartment/<str:id>',views.deletedepartment, name="deletedepartment"),
    
    path('designation/',views.designation, name="designation"),
    path('adddesignation/',views.adddesignation, name="adddesignation"),
    path('editdesignation/',views.editdesignation, name="editdesignation"),
    path('updatedesignation/<str:id>',views.updatedesignation, name="updatedesignation"),
    path('deletedesignation/<str:id>',views.deletedesignation, name="deletedesignation"),
    
    path('level/',views.level, name="level"),
    path('addlevel/',views.addlevel, name="addlevel"),
    path('editlevel/',views.editlevel, name="editlevel"),
    path('updatelevel/<str:id>',views.updatelevel, name="updatelevel"),
    path('deletelevel/<str:id>',views.deletelevel, name="deletelevel"),
    
    path('employee/',views.employee, name="employee"),
    path('addemployee/',views.addemployee, name="addemployee"),
    path('editemployee/',views.editemployee, name="editemployee"),
    path('updateemployee/<str:id>',views.updateemployee, name="updateemployee"),
    path('deleteemployee/<str:id>',views.deleteemployee, name="deleteemployee"),

]