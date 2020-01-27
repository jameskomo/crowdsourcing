from django.db import models
from django.contrib.auth.models import User
from users.models import Grade
from users.validators import validate_file_extension



class Project(models.Model):
    project_name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500, default=None)
    postedOn = models.DateTimeField(auto_now_add=True, blank=True)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    isCompleted = models.BooleanField(default=False)
    deadline = models.DateTimeField(blank=True, null=True)
    task_count = models.IntegerField(default=0)
    attachments=models.FileField(default='Attach Workdone', upload_to='tasks_docs', validators=[validate_file_extension])


    def __str__(self):
        return self.project_name

class Task(models.Model):
    task_name = models.CharField(max_length=50, blank=False)
    addedOn = models.DateTimeField(auto_now_add=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)
    amount = models.IntegerField(default=0)
    task_description = models.TextField(max_length=1000, default=None)
    task_link = models.URLField(blank=True)
    latest_submission_time = models.DateTimeField(blank=True, null=True)
    isCompleted = models.BooleanField(default=False)
    deadline = models.DateTimeField(blank=True, null=True)
    task_attachments=models.FileField(default='Attach Workdone', upload_to='tasks_docs', validators=[validate_file_extension])

    def __str__(self):
        return self.task_name

