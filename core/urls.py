from django.urls import path
from . import views

urlpatterns = [
    path('lists/', views.TaskListListCreate.as_view()),
    path('lists/<int:pk>/', views.TaskListRetrieveUpdateDestroy.as_view()),
    path('lists/<int:pk>/tasks/', views.TaskListCreate.as_view()),
    path('lists/<int:list_pk>/tasks/<int:pk>/', views.TaskRetrieveUpdateDestroy.as_view()),
]
