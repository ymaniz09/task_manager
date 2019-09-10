from django.urls import path

from app.views import list_tasks, add_task

urlpatterns = [
    path('list_tasks/', list_tasks, name='list_tasks'),
    path('add_task/', add_task, name='add_tasks'),
]
