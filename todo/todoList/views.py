from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


from .models import Todo


def index(request):
    latest_todo_list = Todo.objects.order_by('-deadline_date')[:5]
    context = {
        'latest_todo_list': latest_todo_list,
    }
    return render(request, 'todoList/index.html', context)


def editieren(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'todoList/editieren.html', {'todo': todo})


def erstellen(request):
    return render(request, 'todoList/erstellen.html')


def impressum(request):
    return render(request, 'todoList/impressum.html')

