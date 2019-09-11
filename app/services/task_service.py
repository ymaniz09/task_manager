from ..models import Tasks


def store_task(task):
    Tasks.objects.create(title=task.title,
                         description=task.description,
                         expiration_date=task.expiration_date,
                         priority=task.priority)


def list_tasks():
    return Tasks.objects.all()


def list_task_id(task_id):
    return Tasks.objects.get(id=task_id)


def edit_task(stored_task, edited_task):
    stored_task.title = edited_task.title
    stored_task.description = edited_task.description
    stored_task.expiration_date = edited_task.expiration_date
    stored_task.priority = edited_task.priority
    stored_task.save(force_update=True)


def remove_task(stored_task):
    stored_task.delete()
