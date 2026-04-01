from django.shortcuts import  render , get_object_or_404, redirect

from tasks.forms import TaskForm #Importujemy nowy formularz
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
     # Jesli klinie to POST koniecznie
    if request.method == 'POST':
       form = TaskForm(request.POST) #Wypelni okienko
       if form.is_valid(): #Sprawdz czy jest ok
          task = form.save(commit=False) #Zapisz ale nie commituj
          task.project = project #Przypisz zadanko do projektu
          task.save() #Zapisz zadanie na stale 
          return redirect('project_detail', pk=project.pk) #Odśwież strone projektu zeby zobaczyc nowe zadanie
       
    else:
        #jesli tylko wszedł dajemy get
        form = TaskForm() #Pusty formularz

    tasks = Task.objects.filter(project=project) #Pobierz zadania dla tego projektu

    return render(request, 
                  'projects/project_detail.html',{
                        'project': project, 
                        'tasks': tasks, 
                        'form': form #Dajemy do HTML
                  })

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id) #Pobierz zadanie
    task.status = 'Done' #Zmiana na zrobione
    task.save() #Zapisz zmiany

    return redirect('project_detail', pk=task.project.pk) #Uzytkownik wraca do torny projektu z zadaniem

