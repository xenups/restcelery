from django.conf.urls import url
from rest_framework import routers

from App import views
from django.urls import path, include

urlpatterns = [
    path('tasks/', views.TaskLists.as_view(report="hello mashti")),
    path('tasks/<int:pk>/', views.TaskDetails.as_view()),
]
