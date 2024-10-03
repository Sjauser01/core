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

    path('classification/',views.classification, name="classification"),
    path('addclassification/',views.addclassification, name="addclassification"),
    path('editclassification/',views.editclassification, name="editclassification"),
    path('updateclassification/<str:id>',views.updateclassification, name="updateclassification"),
    path('deleteclassification/<str:id>',views.deleteclassification, name="deleteclassification"),

    path('suffix/',views.suffix, name="suffix"),
    path('addsuffix/',views.addsuffix, name="addsuffix"),
    path('editsuffix/',views.editsuffix, name="editsuffix"),
    path('updatesuffix/<str:id>',views.updatesuffix, name="updatesuffix"),
    path('deletesuffix/<str:id>',views.deletesuffix, name="deletesuffix"),

    path('prefix/',views.prefix, name="prefix"),
    path('addprefix/',views.addprefix, name="addprefix"),
    path('editprefix/',views.editprefix, name="editprefix"),
    path('updateprefix/<str:id>',views.updateprefix, name="updateprefix"),
    path('deleteprefix/<str:id>',views.deleteprefix, name="deleteprefix"),

    path('setup/',views.setup, name="setup"),
    path('addsetup/',views.addsetup, name="addsetup"),
    path('save-form-data/', views.save_form_data, name='save_form_data'),

    path('plant/',views.plant, name="plant"),
    path('addplant/',views.addplant, name="addplant"),
    path('editplant/',views.editplant, name="editplant"),
    path('updateplant/<str:id>',views.updateplant, name="updateplant"),
    path('deleteplant/<str:id>',views.deleteplant, name="deleteplant"),

    path('storage/',views.storage, name="storage"),
    path('addstorage/',views.addstorage, name="addstorage"),
    path('editstorage/',views.editstorage, name="editstorage"),
    path('updatestorage/<str:id>',views.updatestorage, name="updatestorage"),
    path('deletestorage/<str:id>',views.deletestorage, name="deletestorage"),

]