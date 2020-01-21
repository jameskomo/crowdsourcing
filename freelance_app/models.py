from django.db import models
from django.contrib.auth.models import User
from users.models import Grade





class Task(models.Model):
    task_name = models.CharField(max_length=50, blank=False)
    addedOn = models.DateTimeField(auto_now_add=True, blank=True)
    # project = models.ForeignKey(Project, on_delete=models.CASCADE)
    rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)
    amount = models.IntegerField(default=0)
    task_description = models.CharField(max_length=100, default=None)
    task_link = models.URLField(blank=True)
    latest_submission_time = models.DateTimeField(blank=True, null=True)
    isCompleted = models.BooleanField(default=False)
    deadline = models.DateField(blank=False)

    def __str__(self):
        return self.task_name

class Project(models.Model):
    project_name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=300, default=None)
    postedOn = models.DateTimeField(auto_now_add=True, blank=True)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    isCompleted = models.BooleanField(default=False)
    deadline = models.DateField(blank=False)
    tasks=models.ForeignKey(Task, on_delete=models.CASCADE)
    task_count = models.IntegerField(default=0)


    def __str__(self):
        return self.project_name