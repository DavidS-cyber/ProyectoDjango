from django.urls import path
from .views import TaskListCreate, TaskListDelete, TaskCreate, TaskDetail

urlpatterns = [
    # Rutas para las Listas
    path('lists/', TaskListCreate.as_view()),
    path('lists/<int:pk>/', TaskListDelete.as_view()),
    
    # Rutas para las Tareas
    path('lists/<int:list_id>/tasks/', TaskCreate.as_view()),
    path('lists/<int:list_id>/tasks/<int:task_id>/', TaskDetail.as_view()),
]