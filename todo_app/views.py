from django.shortcuts import render
from .models import *

# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items' : items
    }
    return render(request, 'todo_app/todo_list.html', context=context)

def add_item(request):
    
    return render(request, 'todo_app/add_item.html')
