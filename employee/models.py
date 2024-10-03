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


class Classification(models.Model):
    classification_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    classification_status = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Suffix(models.Model):
    suffix_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    suffix_status = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Prefix(models.Model):
    prefix_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    prefix_status = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Series(models.Model):
    field1 = models.CharField(max_length=50, blank=True, null=True)
    field2 = models.CharField(max_length=50, blank=True, null=True)
    field3 = models.CharField(max_length=50, blank=True, null=True)
    field4 = models.CharField(max_length=50, blank=True, null=True)
    field5 = models.CharField(max_length=50, blank=True, null=True)
    field6 = models.CharField(max_length=50, blank=True, null=True)
    field7 = models.CharField(max_length=50, blank=True, null=True)
    field8 = models.CharField(max_length=50, blank=True, null=True)
    field9 = models.CharField(max_length=50, blank=True, null=True)
    field10 = models.CharField(max_length=50, blank=True, null=True)
    field11 = models.CharField(max_length=50, blank=True, null=True)
    field12 = models.CharField(max_length=50, blank=True, null=True)
    field13 = models.CharField(max_length=50, blank=True, null=True)
    field14 = models.CharField(max_length=50, blank=True, null=True)
    field15 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"FormData: {self.id}"

class CompAndBOM(models.Model):
    choice1 = models.CharField(max_length=50)
    choice2 = models.CharField(max_length=50)
    choice3 = models.CharField(max_length=50)
    choice4 = models.CharField(max_length=50)

    def __str__(self):
        return f"CompAndBOM: {self.id}"

class Plant(models.Model):
    plant_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    plant_status = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Storage(models.Model):
    storage_code = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    storage_type = models.CharField(max_length=10)
    dimension = models.CharField(max_length=20)

    def __str__(self):
        return self.name