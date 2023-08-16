from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or none)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
        messages.success(request, ("New Task Added!"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(manage=request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('page')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request, ("Access Restricted, You are not allowed!"))

    return redirect('todolist')

@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ("Access Restricted, You are not allowed!"))

    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()

    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Edited!"))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

def index(request):
    contact = {
        'index_text':"Welcome to the Taskmate Home page"
    }
    return render(request, 'index.html', contact)

def contact(request):
    contact = {
        'welcome_text':"Welcome to my contact page"
    }
    return render(request, 'contact.html', contact)

def about(request):
    about = {
        'about_text':"Welcome to my about page"
    }
    return render(request, 'about.html', about)