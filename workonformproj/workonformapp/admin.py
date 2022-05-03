from django.contrib import admin
from .models import Country, City, Student
# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Student)