from django.shortcuts import render, get_object_or_404, redirect  # ✅ ajouté get_object_or_404 et redirect
from .models import Task
from .forms import TaskForm

# Afficher toutes les tâches
def task_list(request):
    tasks = Task.objects.all().order_by('-id')  # les plus récentes en premier
    return render(request, 'todo_app/task_list.html', {'tasks': tasks})

# Afficher une tâche
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo_app/task_detail.html', {'task': task})

# Créer une tâche
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo_app/task_form.html', {'form': form})

# Mettre à jour une tâche
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo_app/task_form.html', {'form': form})

# Supprimer une tâche
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo_app/task_detail.html', {'task': task})

# Basculer l'état complété/non complété
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

from django.db import models
from django.utils import timezone

created_at = models.DateTimeField(default=timezone.now)  # <-- correct








# Create your views here.
