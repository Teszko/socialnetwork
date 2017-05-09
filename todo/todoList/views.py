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


def change(request, question_id):
    response = "You're about to change a TodoItem %s."
    return HttpResponse(response % question_id)

def create(request, question_id):
    return HttpResponse("You're creating a TodoItem %s." % todoId_id)

