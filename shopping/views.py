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
