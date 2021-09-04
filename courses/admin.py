from django.contrib import admin
from .models import Subject, Course, Module
from .models import Student, Teacher
from .models import *


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    # prepopulated_fields = {('slug'): 'title'}

class ModuleInLine(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    # prepopulated_fields = {('slug'): 'title'}
    inlines = [ModuleInLine]

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Exam)
admin.site.register(Homework)
admin.site.register(HomeworkAnswer)