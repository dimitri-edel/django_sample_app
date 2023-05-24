from django.shortcuts import render, redirect
from .models import *
from .forms import ItemForm

# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items' : items
    }
    return render(request, 'todo_app/todo_list.html', context=context)

def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

    form = ItemForm()
    context = {
        'form' : form
    }
    return render(request, 'todo_app/add_item.html', context=context)
