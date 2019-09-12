from django.shortcuts import render, redirect

from app.entities.task import Task
from app.forms import TaskForm
from app.services import task_service


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


def edit_task(request, task_id):
    stored_task = task_service.list_task_id(task_id)
    task_form = TaskForm(request.POST or None, instance=stored_task)

    if task_form.is_valid():
        title = task_form.cleaned_data["title"]
        description = task_form.cleaned_data["description"]
        expiration_date = task_form.cleaned_data["expiration_date"]
        priority = task_form.cleaned_data["priority"]

        edited_task = Task(title=title, description=description, expiration_date=expiration_date, priority=priority)
        task_service.edit_task(stored_task, edited_task)

        return redirect('list_tasks')

    return render(request, 'tasks/form_task.html', {'task_form': task_form})


def remove_task(request, task_id):
    stored_task = task_service.list_task_id(task_id)

    if request.method == "POST":
        task_service.remove_task(stored_task)
        return redirect('list_tasks')

    return render(request, 'tasks/confirm_exclusion.html', {'task': stored_task})
