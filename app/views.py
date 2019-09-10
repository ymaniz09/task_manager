from django.shortcuts import render, redirect

from app.entities.task import Task
from .forms import TaskForm
from .services import task_service


# Create your views here.
def list_tasks(request):
    return render(request, 'tasks/list_tasks.html', {'tasks': task_service.list_tasks()})


def add_task(request):
    if request.method == "POST":

        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            title = task_form.cleaned_data["title"]
            description = task_form.cleaned_data["description"]
            expiration_date = task_form.cleaned_data["expiration_date"]
            priority = task_form.cleaned_data["priority"]

            task_service.store_task(
                Task(title=title, description=description, expiration_date=expiration_date, priority=priority))

            return redirect('list_tasks')

    else:
        task_form = TaskForm(request.POST)
        return render(request, 'tasks/form_task.html', {'task_form': task_form})
