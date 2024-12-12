from django.shortcuts import render, redirect

from tasks.forms import TaskCreateForm, TaskForm
from tasks.models import Project, User, Task, TaskStatus


def index(request):
  return render(request, 'tasks/index.html')

def projects(request):
  projects_list = Project.objects.all()
  return render(request, 'project/list.html', context={'projects': projects_list})

def performers(request):
  performers_list = User.objects.all()
  return render(request, 'tasks/performers.html', context={'performers': performers_list})

def tasks(request):
  tasks_list = Task.objects.all()
  return render(request, 'tasks/list.html', context={'tasks': tasks_list})

def project(request, project_id):
  project_view = Project.objects.get(pk=project_id)
  tasks_list = Task.objects.filter(project_id=project_id)
  return render(request, 'project/detail.html', context={'project': project_view, 'tasks': tasks_list})

def create_project(request):
  if request.method == 'POST':
    name = request.POST['name']
    description = request.POST['description']
    project_view = Project.objects.create(name=name, description=description)
    return redirect('project', project_view.id)
  return render(request, 'project/create.html')


def create_task(request):
  if request.method == "POST":
    form = TaskCreateForm(request.POST)
    if form.is_valid():
      # form.save()  # В случае если не нужно изменять сущность задачи
      task = form.save(commit=False)
      task.status = TaskStatus.objects.get(name="Новая")
      task.save()
      return redirect('tasks')
  else:
    form = TaskCreateForm()

  projects_list = Project.objects.all()
  return render(request, 'tasks/create.html', context={'form': form, 'projects': projects_list})

def task(request, task_id):
  task_view = Task.objects.get(pk=task_id)  # Получаем объект Task по первичному ключу
  if request.method == "POST":
    form = TaskForm(request.POST, instance=task_view)  # Передаём существующий объект в форму
    if form.is_valid():
      form.save()
      return redirect('tasks')
  else:
    form = TaskForm(instance=task_view)  # Предзаполняем форму текущими данными
  return render(request, 'tasks/details.html', {'form': form, 'task': task})