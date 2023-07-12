from django.shortcuts import render , redirect
from .models import todoList
from .forms import todoList_forms
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    todo_items = todoList.objects.order_by('id')
    form = todoList_forms()
    context = {'todo_items':todo_items, 'form':form}
    return render(request, 'todoList/index.html', context)
@require_POST
def addTodoItem(request):
    form =todoList_forms(request.POST)

    if form.is_valid():
        newtodo =todoList(text =request.POST['text'])
        newtodo.save()

    return redirect ('index')

def completedTodo(request , todo_id):
    todo =todoList.objects.get(pk=todo_id)
    todo.completed=True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    todoList.objects.filter(completed__exact=True).delete()

    return redirect ('index')

def deleteAll(request):
    todoList.objects.all().delete()

    return redirect ('index')
