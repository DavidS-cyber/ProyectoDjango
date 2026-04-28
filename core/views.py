from rest_framework import generics
from .models import TaskList, Task
from .serializers import TaskListSerializer, TaskSerializer


class TaskListListCreate(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskListCreate(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(task_list_id=self.kwargs['pk'])

    def perform_create(self, serializer):
        task_list = TaskList.objects.get(pk=self.kwargs['pk'])
        serializer.save(task_list=task_list)


class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(task_list_id=self.kwargs['list_pk'])
