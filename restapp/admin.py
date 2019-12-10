from django.contrib import admin
from restapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['sid','sname','sadd']

admin.site.register(Student,StudentAdmin)
