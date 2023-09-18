from rest_framework import serializers
from .models import TaskApp

class TaskAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskApp
        fields = ( 'id', 'task_title', 'task_description', 
                  'task_isCompleted' )

