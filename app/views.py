from django.shortcuts import render, redirect

from app.entities.task import Task
from .forms import TaskForm
from .services.task_service import store_task


# Create your views here.
def list_tasks(request):
    task_name = "Finish Django project"
    return render(request, 'tasks/list_tasks.html', {'task_name': task_name})


def add_task(request):
    if request.method == "POST":

        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            title = task_form.cleaned_data["title"]
            description = task_form.cleaned_data["description"]
            expiration_date = task_form.cleaned_data["expiration_date"]
            priority = task_form.cleaned_data["priority"]

            store_task(Task(title=title, description=description, expiration_date=expiration_date, priority=priority))

            return redirect('list_tasks')

    else:
        task_form = TaskForm(request.POST)
        return render(request, 'tasks/form_task.html', {'task_form': task_form})
