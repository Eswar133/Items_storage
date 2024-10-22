from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
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

    # Sorting
    sort_by = request.GET.get('sort_by', 'name')  # Default sorting by name
    items = items.order_by(sort_by)

    # Pagination
    paginator = Paginator(items, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'items/item_list.html', {'page_obj': page_obj, 'sort_by': sort_by})
