from django.shortcuts import render
from .models import Project
from tasks.models import Task


def project_list(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()

    print(f"Znaleziono projektów : {projects.count()}")
    

    return render(request, 'projects/project_list.html', {'projects': projects, 'tasks': tasks})
