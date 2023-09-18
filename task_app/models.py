from django.db import models

class TaskApp(models.Model):

    task_title = models.CharField(max_length=120)
    task_description = models.CharField(max_length=120)
    task_isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.task_title
