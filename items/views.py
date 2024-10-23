from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Item


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True  


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login') 


@login_required
def item_list(request):
    items = Item.objects.all()

    
    sort_by = request.GET.get('sort_by', 'name')  # Default 
    items = items.order_by(sort_by)

    
    paginator = Paginator(items, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'items/item_list.html', {'page_obj': page_obj, 'sort_by': sort_by})

@login_required
def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        
        if not name or not price:
            messages.error(request, 'Name and Price are required.')
        else:
            try:
                price = float(price)
                item = Item.objects.create(name=name, description=description, price=price)
                item.save()
                messages.success(request, 'Item added successfully!')
                return redirect('item_list')
            except ValueError:
                messages.error(request, 'Invalid price format.')
    
    return render(request, 'items/add_item.html')