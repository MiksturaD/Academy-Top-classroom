from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import FeedbackModelForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        Product.objects.create(name=name, description=description, price=price)
        return redirect('product_list')
    return render(request, 'products/add_product.html')

def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.save()
        return redirect('product_list')
    return render(request, 'products/edit_product.html', {'product': product})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_list')

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackModelForm(request.POST)
        if form.is_valid():
            form.save()  # Автоматически сохраняет данные в базу
            return redirect('thank_you')
    else:
        form = FeedbackModelForm()
    return render(request, 'feedback.html', {'form': form})