from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from App import serializers
from App.models import Task


class TaskLists(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer

    report = None

    def get_object(self, queryset=None):
        return queryset.get(report=self.report)


class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
