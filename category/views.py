from django.shortcuts import render, redirect
from .models import Category
from .forms import categoryForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})

def create_category(request):
    if request.method == 'POST':
        form = categoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # Redirect to the category list page after creating a new category
    else:
        form = categoryForm()
    return render(request, 'category/create_category.html', {'form': form})
