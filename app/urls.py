from django.urls import path

from app.views import list_tasks, add_task, edit_task

urlpatterns = [
    path('list_tasks/', list_tasks, name='list_tasks'),
    path('add_task/', add_task, name='add_tasks'),
    path('edit_task/<int:task_id>', edit_task, name='edit_tasks'),
]
