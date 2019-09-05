from django.urls import path

from app.views import list_tasks

urlpatterns = [
    path('list_tasks/', list_tasks, name='list_tasks'),
]
