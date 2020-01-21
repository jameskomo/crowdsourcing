from django.shortcuts import render, redirect
from .models import Project, Task
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User
from .models import *


# Create your views here.
def home(request):
    return render(request, 'freelance_app/base.html')

def projects(request, project_id, task_id):
    projects_list = Project.objects.all()
    number_of_projects=Project.objects.all().count
    number_of_tasks=Task.objects.all().count
    tasks = Task.objects.get(id=task_id, project=project_id)
    
    # project_tasks=Task.objects.filter(project_id__in=Project.objects.all()).order_by('latest_submission_time')
    project_tasks=Task.objects.all() 
    context={
        'projects_list': projects_list,
        'number_of_projects':number_of_projects,
        'project_tasks': project_tasks,
        'tasks': tasks
    }
    return render(request, "freelance_app/projects.html", context)


# VIEW FUNCTIONS


# List Views for Project, Tasks...

class ProjectListView(ListView):
    model = Project
    template_name = 'freelance_app/projects.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-postedOn']


#  Update Class Views for Project, Task, ....

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['project_name', 'description', 'deadline', 'tasks']
    success_url="/projects/"

    def form_valid(self, form):
        form.instance.Owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.Owner:
            return True
        return False


# Detail Views for Post, Business, Neighborhood and Contact
class ProjectDetailView(DetailView):
    model = Project


# Create Views for Project, Tasks.....
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['project_name', 'description', 'Owner', 'deadline', 'tasks']
    success_url="/projects/"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)



# Delete Class Views for Profile, Task...
class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/projects'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.Owner:
            return True
        return False


def tasks_edit(request, project_id, task_id):
    if request.user.is_authenticated:
        task = Task.objects.get(id=task_id, project=project_id)
        print(task)
        project = Project.objects.get(id=project_id)
        context = {}
        context['task'] = task
        context['project'] = project
        if request.method == 'POST':
            task.task_name = request.POST['name']
            task.task_description = request.POST['description']
            task.save()
            return redirect("kinetic-projects", project_id, task_id)
        project = Project.objects.get(id=project_id)
        return render(request,'freelance_app/edittask.html',context)
    return redirect("kinetic-projects", project_id, task_id)