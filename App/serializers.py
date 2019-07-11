from rest_framework import serializers

from App.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'report',)

    def create(self, validated_data):
        # first we pop or get the the type of the data we want
        task = Task.objects.create(**validated_data)
        task.title = validated_data['title']
        task.report_data = validated_data['report']
        # tasker()
        task.save()
        return task
#its simply shows that how its called
#but we want  call our task via signal
#when our model created it signal to proccess the task
# def tasker():
#     print("salam golabi")
#     process.delay()
#     # girkone()
