from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.urls import reverse

from .models import Todo


def index(request):
    latest_todo_list = Todo.objects.order_by('-deadline_date')
    # latest_todo_list = Todo.objects.order_by('-deadline_date')[:5]
    for element in latest_todo_list:
        element.deadline_date = element.deadline_date.strftime("%d.%m.%Y")
    return render(request, 'todoList/index.html', {'latest_todo_list': latest_todo_list})


def editieren(request, todo_id):
    todo_request = get_object_or_404(Todo, pk=todo_id)
    todo_request.deadline_date = todo_request.deadline_date.strftime("%Y-%m-%d")
    return render(request, 'todoList/editieren.html', {'todo': todo_request})


def erstellen(request):
    return render(request, 'todoList/erstellen.html')


def impressum(request):
    return render(request, 'todoList/impressum.html')


def save(request, todo_id=None):
    submitted_todo_text = request.POST.get('todo_text', '<<post error>>')
    submitted_deadline_date = request.POST.get('deadline_date', '2000-1-1')
    submitted_percentage = int(request.POST.get('percentage', 0))

    if todo_id is None:
        submitted_todo = Todo(percentage=submitted_percentage, todo_text=submitted_todo_text, deadline_date=submitted_deadline_date, )
        submitted_todo.save()
    else:
        pass
        change_todo = get_object_or_404(Todo, pk=todo_id)
        change_todo.percentage = submitted_percentage
        change_todo.todo_text = submitted_todo_text
        change_todo.deadline_date = submitted_deadline_date
        change_todo.save()

    return HttpResponseRedirect(reverse('todoList:index'))


def delete(request, todo_id):
    delete_todo = get_object_or_404(Todo, pk=todo_id)
    delete_todo.delete()
    return HttpResponseRedirect(reverse('todoList:index'))

