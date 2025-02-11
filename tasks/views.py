from django.shortcuts import render,redirect, get_object_or_404
from .models import Task

# Display all tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
# home view
def home(request):
    if request.method == 'POST':
        return redirect('task_list')
    return render(request, 'tasks/home.html')
# Create a new task
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'tasks/task_form.html')

def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'task': task})
# Delete task view
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
#user login details
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            return redirect('home')
    return render(request, 'tasks/login.html')