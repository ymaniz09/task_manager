from django.urls import path

from app.views.task_views import list_tasks, add_task, edit_task, remove_task
from app.views.users_views import sign_up

urlpatterns = [
    path('list_tasks/', list_tasks, name='list_tasks'),
    path('add_task/', add_task, name='add_tasks'),
    path('edit_task/<int:task_id>', edit_task, name='edit_task'),
    path('remove_task/<int:task_id>', remove_task, name='remove_task'),
    path('signup/', sign_up, name='remove_task'),
]
