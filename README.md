Información del trabajo 
# Gestor de Listas de Tareas con Django
API REST desarrollada con Django y Django REST Framework.
## Requisitos
- Python
- Django
- Django REST Framework
## Instalación
pip install django djangorestframework
## Ejecución
py manage.py runserver
## Endpoints
### Listas de tareas
- GET /lists/ — Obtener todas las listas
- POST /lists/ — Crear una lista
- DELETE /lists/<id>/ — Eliminar una lista
### Tareas
- GET /lists/<id>/tasks/ — Obtener tareas de una lista
- POST /lists/<id>/tasks/ — Añadir una tarea
- PATCH /lists/<id>/tasks/<id>/ — Marcar tarea como completada
- DELETE /lists/<id>/tasks/<id>/ — Eliminar una tarea
  
