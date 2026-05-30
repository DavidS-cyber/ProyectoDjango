from rest_framework import generics
from .models import TaskList, Task
from .serializers import TaskListSerializer, TaskSerializer

class TaskListCreate(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

class TaskListDelete(generics.DestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

class TaskCreate(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(task_list_id=self.kwargs['list_id'])

    def perform_create(self, serializer):
        serializer.save(task_list_id=self.kwargs['list_id'])

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'task_id'
