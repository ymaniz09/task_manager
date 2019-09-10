from ..models import Tasks


def store_task(task):
    Tasks.objects.create(title=task.title,
                         description=task.description,
                         expiration_date=task.expiration_date,
                         priority=task.priority)


def list_tasks():
    return Tasks.objects.all()
