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
from .models import Task, Grade, Project
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request, 'freelance_app/base.html')

def projects(request, project_id, task_id):
    projects_list = Project.objects.all()
    number_of_projects=Project.objects.all().count
    context={
        'projects_list': projects_list,
        'number_of_projects':number_of_projects,
    }
    return render(request, "freelance_app/projects.html", context)

def tasks(request, project_id, task_id):
    tasks_list = Task.objects.all()
    number_of_tasks=Task.objects.all().count
    context={
        'tasks_list': tasks_list,
        'number_of_tasks':number_of_projects,
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
    fields = ['project_name', 'description', 'deadline']
    success_url="/projects/"

    def form_valid(self, form):
        form.instance.Owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.Owner:
            return True
        return False


# Detail Views for Project, Tasks....
class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the Tasks
        context['task_list'] = Task.objects.all()
        return context


# Create Views for Project, Tasks.....
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['project_name', 'description', 'Owner', 'deadline']
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


# Task Views
class TaskCreate(CreateView):
    model = Task
    fields = ['project', 'task_name', 'task_description', 'latest_submission_time', 'deadline','isCompleted']
    success_url="/task/add"

class TaskUpdate(UpdateView):
    model = Task
    fields = ['project','task_name', 'task_description', 'latest_submission_time', 'deadline', 'isCompleted']

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('profile-list')
class TaskDetail(DetailView):
    model=Task

# SEARCH VIEWS
class ProjectResultsView(ListView):
    model = Project
    template_name = 'project_list.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        project_list = Project.objects.filter(
            Q(project_name__icontains=query) | Q(description__icontains=query)
        )
        return project_list

