from django.shortcuts import render, redirect
from .models import Task

def home(request):
    if request.method == 'POST':
        new_task = Task(name=request.POST['name'])
        new_task.save()
        return redirect('home')
    else:
        tasks = Task.objects.all()
        return render(request, 'home.html', {'tasks': tasks})

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')