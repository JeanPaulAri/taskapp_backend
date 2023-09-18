from django.contrib import admin
from .models import TaskApp

class TaskAppAdmin(admin.ModelAdmin):
    list_display =  ("task_title", "task_description", "task_isCompleted")

#register model

admin.site.register(TaskApp, TaskAppAdmin)
