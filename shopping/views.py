from django.shortcuts import render,redirect
from .forms import ItemForm
from .models import ShoppingList


def index(request):
    items = ShoppingList.objects.all()  
    return render(request, 'index.html', {'items': items})


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm()
    return render(request, 'add.html', {'form': form})

    
def shopping_list (request):
    items = ShoppingList.objects.all()
    return render(request,'shopping_list.html',{'items':items})


def edit_item(request,item_id):
    item = ShoppingList.objects.get(id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/add')
    else:
        form = ItemForm(instance=item)
    return render(request, 'edit.html', {'form': form})