from django.shortcuts import render , get_object_or_404 
from .models import Project
from tasks.models import Task


def project_list(request):

    projects = Project.objects.all()
    tasks = Task.objects.all()

    return render(request, 
                  'projects/project_list.html', 
                  {'projects': projects, 'tasks': tasks})


def project_detail(request, pk):

    project = get_object_or_404(Project, pk=pk)
    tasks = Task.objects.filter(project=project)

    return render(request, 
                  'projects/project_detail.html', 
                  {'project': project, 'tasks': tasks})