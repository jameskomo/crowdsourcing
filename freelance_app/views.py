from django.shortcuts import render
from .models import Project, Task

# Create your views here.
def home(request):
    return render(request, 'freelance_app/base.html')

def projects(request):
    projects_list = Project.objects.all()
    number_of_projects=Project.objects.all().count
    # project_tasks=Task.objects.filter(project_id__in=Project.objects.all()).order_by('latest_submission_time')
    project_tasks=Task.objects.all()
    context={
        'projects_list': projects_list,
        'number_of_projects':number_of_projects,
        'project_tasks': project_tasks
    }
    return render(request, "freelance_app/projects.html", context)
