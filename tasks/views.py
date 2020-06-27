from django.shortcuts import render, redirect
from .models import Item
from .forms import *

# Create your views here.
def home(request):

    # Get all items in the DB
    items = Item.objects.all()
    
    # Forms
    form = ItemForm()

    if request.method == 'POST':
        # When the user click on the button
        form = ItemForm(request.POST)
        if form.is_valid():    
            form.save()     # Save item in the database
        return redirect('/')    # Redirect to the page but using the GET method



    context = {
        'items': items,
        'form': form,

    }
    return render(request, 'tasks/index.html', context)


# To update an item
def update_item(request, pk):

    # Get the item with the primary key: pk
    item = Item.objects.get(id=pk)

    form = ItemForm(instance=item)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():    
            form.save()     # Save item in the database
            return redirect('/')    # Redirect to the page but using the GET method

    context = {
        'form': form

    }
    return render(request, 'tasks/update.html', context)



def delete_item(request, pk):
    
    # Delete in the database
    # Get the item with the primary key: pk
    item = Item.objects.get(id=pk)

    # Receive the POST ie receive the confirmation button to delete the item
    if request.method == 'POST':
        item.delete()
        return redirect('/')


    context = {
        'item': item,

    }

    return render(request, 'tasks/delete.html', context)