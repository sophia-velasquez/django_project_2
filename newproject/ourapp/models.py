from django.db import models
from datetime import datetime


class School(models.Model):
    name = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    postal_code = models.IntegerField()

    def __str__(self):
        return self.name


class Certificate_Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=40)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    graduation_date = models.DateField(default=datetime.today)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    grade = models.CharField(max_length=40)
    School = models.ForeignKey(School, on_delete=models.PROTECT)
    Certificate_Type = models.ForeignKey(Certificate_Type, on_delete=models.PROTECT)

    def __str__(self):
        return self.full_name
