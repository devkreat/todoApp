from django.shortcuts import render
from .models import todoList

# Create your views here.
def index(request):
    todo_items = todoList.objects.order_by('id')
    context = {'todo_items':todo_items}
    return render(request, 'todoList/index.html', context)
