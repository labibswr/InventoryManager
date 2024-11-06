from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, Sum
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages

# Create your views here.

# Security feature added for admin login requirement to view these pages
@login_required
def index(request):
    # Showing user's requests and allowing student to make request for borrowing item
    loans = Loan.objects.all()
    items = Item.objects.all()
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance= form.save(commit=False)
            # Assigning the current user/student to this check out
            instance.student = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()

    # Dash head numbers
    total_items = Item.objects.count()
    item_quantity = Item.objects.aggregate(total=Sum('quantity'))['total']
    total_loans = Loan.objects.count()
    loan_quantity = Loan.objects.aggregate(total=Sum('order_quantity'))['total']

    # Graphs code
    # Count of items in each category
    cat_count = Item.objects.values('category').annotate(item_count=Count('category'))

    # Data
    categories = [item['category'] for item in cat_count]
    num_cat = [item['item_count'] for item in cat_count]

    context = {
        'loans': loans,
        'form': form,
        'items': items,
        'total_items': total_items,
        'item_quantity': item_quantity,
        'total_loans': total_loans,
        'loan_quantity': loan_quantity,
        'categories': categories,
        'num_cat': num_cat
    }
    # This function renders the index html but the if statement on that html
    # file will render the student index if the student is logged in.
    return render(request, 'DashPages/index.html', context)

@login_required
def item(request):
    # Adding an item to inventory and displaying full inventory list
    items = Item.objects.all()

    # Filtering the items table by category
    # Get the selected category from the GET parameters
    selected_category = request.GET.get('category')

    # Get all unique categories from the items
    categories = Item.objects.values_list('category', flat=True).distinct()

    if selected_category:
        # Filter items by the selected category
        items = Item.objects.filter(category=selected_category)
    else:
        # If no category is selected, show all items
        items = Item.objects.all() 

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid:
            form.save()
            item_name = form.cleaned_data.get('name')
            messages.success(request, f"{item_name} has been successfully added")
            return redirect('dashboard-item')
    else:
        form = ItemForm()

    context = {
        'items': items,
        'form': form,
        'categories': categories
    }

    return render(request, 'DashPages/item.html', context)


# Dashhead numbers
def dash_head(request):
    items = Item.objects.all()
    context = {
        'total': len(items)
    }

    return render(request, 'DashPages/dash_head.html', context)


# Deleting products from inventory
def delete_item(request, pk):
    item = Item.objects.get(id=pk)      # PK => 'primary key'

    if request.method=='POST':
        item.delete()
        return redirect('dashboard-item')

    return render(request, 'DashPages/delete_item.html')

# Editing product details in system
def edit_item(request, pk):
    item = Item.objects.get(id=pk)
    if request.method=='POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-item')
    else:
        form = ItemForm(instance=item)
    context = {
        'form':form
    }
    return render(request, 'DashPages/edit_item.html', context)
    

@login_required
def loan(request):
    borrowed = Loan.objects.all()
    context = {
        'borrowed': borrowed
    }
    return render(request, 'DashPages/loan.html', context)

# Signed out item being returned
@login_required
def returned(request, pk):
    borrowed = Loan.objects.get(id=pk)

    if request.method == 'POST':
        borrowed.delete()
        return redirect('dashboard-loan')

    return render(request, 'DashPages/returned.html')
    
