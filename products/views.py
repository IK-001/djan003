from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def quick_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id, available=True)
    context = {'product': product}
    return render(request, 'products/quick_view.html', context)

def home(request):
    categories = Category.objects.all()  # Fetch categories for display
    return render(request, 'home.html', {'categories': categories})
    
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('id')
    query = request.GET.get('q')
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )
    
    # Sorting
    sort = request.GET.get('sort')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'name':
        products = products.order_by('name')
    
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 9)  # 9 products per page
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    return render(request, 'products/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'query': query})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'products/product_detail.html', {'product': product})
