from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskAppSerializer
from .models import TaskApp

class TaskAppView(viewsets.ModelViewSet):
    serializer_class = TaskAppSerializer
    queryset = TaskApp.objects.all()
    
# Create your views here.
