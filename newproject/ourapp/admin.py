from django.contrib import admin
from .models import School, Certificate_Type, Faculty, Department, Student

# Register your models here.


admin.site.register(School)
admin.site.register(Certificate_Type)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Student)
""