from django.shortcuts import render


# Create your views here.
def list_tasks(request):
    task_name = "Finish Django project"
    return render(request, 'tasks/list_tasks.html', {'task_name': task_name})
