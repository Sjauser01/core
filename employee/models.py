from django.db import models

class Location(models.Model):
    location_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    location_status = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Department(models.Model):
    department_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    department_status = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Designation(models.Model):
    designation_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    designation_status = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Level(models.Model):
    level_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    level_status = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user_code = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20,null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    employee_status = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name
