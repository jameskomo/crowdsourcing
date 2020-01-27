from django.urls import path
from . import views
from freelance_app.views import TaskCreate, TaskDelete, TaskUpdate, TaskDetail
from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    ProjectResultsView,
    
)


urlpatterns = [
    path('', views.home, name='kinetic-home'),
    path('projects/', ProjectListView.as_view(), name='kinetic-projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),

    # Task URLS
    path('task/add/', TaskCreate.as_view(), name='task-add'),
    path('task/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name='task-delete'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    # Task URLS End

    # Search on Page
    path('project_search/', ProjectResultsView.as_view(), name='search_projects'),
    # Search End
    
]