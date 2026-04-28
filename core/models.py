from django.db import models


class TaskList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    task_list = models.ForeignKey(
        TaskList,
        related_name='tasks',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
