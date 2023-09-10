from django.shortcuts import render,redirect,get_object_or_404
from .models import Category,Product,ProductComment,Tag
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ProductCommentForm
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.views.decorators.cache import cache_page
from django.contrib import messages

# Create your views here.
# @cache_page(60*15) #15 min
def all_products(request):
    products = Product.objects.all().order_by('-created')[:8]
    return render(request, 'home.html', context={'products': products})


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    comments = ProductComment.objects.all()
    return render(request, 'product/product_detail.html', context={'product': product,'reviews': comments})

# @cache_page(60*15) #15 min
def store(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    count = products.count()

        
    # Paginate the products
    paginator = Paginator(products,10)  # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
        'categories': categories,
        'count':count,
    }
    
    
    return render(request, 'product/store.html', context)



# @cache_page(60*15) #15 min
def product_search(request):
  
    results = Product.objects.all()
    key = request.GET.get('key')
    cat = request.GET.get('category')
    price_min = request.GET.get('minPrice')
    price_max = request.GET.get('maxPrice')
    
    if key:
        results = results.filter(Q(title__icontains=key) | Q(description__icontains=key))
    if cat:
        c= Category.objects.get(name=cat)
        
        results = results.filter(category=c.id)
    if price_max and price_min  :
        
        results = results.filter(price__range=(price_min, price_max))


    count = results.count()
    paginator = Paginator(results, 10)
    page_number = request.GET.get('page')
    results = paginator.get_page(page_number)

    context = {
        'products': results,
        'categories': Category.objects.all(),
        'count': count,
    }
    
    
    return render(request, 'product/store.html', context)


def category(request, slug):
    products = Product.objects.filter(slug=slug)
    return render(request, 'products/category.html', context={'products': products})

def make_sale(request):
    products = Product.objects.exclude(tags__name='sale')
    
    if request.method == 'POST':
        selected_products = request.POST.getlist('selected_products')
        
        for product in selected_products:
            product_obj = Product.objects.get(id=product)
            tag_obj, created = Tag.objects.get_or_create(name="sale")
            product_obj.tags.add(tag_obj.id)
        
        return redirect('products:home')
    
    else:
        return render(request, 'product/productmanage.html', context={'products': products})
 
# def track_product(request):
#     products = Product.objects.filter(set_track = False)
#     if request.method == 'POST':
#         product_link = request.POST.get('link')
#         product_id = request.POST.get('id')
#         print(product_link)
#         product = get_object_or_404(Product, pk=product_id)
#         product.set_on_track(product_link)
#         return redirect(request.META['HTTP_REFERER'])
         
#     else:
#         return render(request, 'product/track.html', {'products':products })
from django.core.mail import send_mail
def mails(request):
    subject = 'Hello, Django Email'
    message = 'This is a test email sent from Django.'
    from_email = 'farag92mohamed@gmail.com'
    recipient_list = ['farag92mohamed@gmail.com']

    send_mail(subject, message, from_email, recipient_list)
    return JsonResponse({"success": True})
# CRM

@login_required(login_url='accounts:login')
def add_comment(request, pk):
    product = get_object_or_404(Product, id=pk)
    
    if request.method == 'POST':
        form = ProductCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = ProductCommentForm()
        
    return redirect(request.META['HTTP_REFERER'])

@login_required(login_url='accounts:login')
def edit_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect('/product/' + str(product_id))
    else:
        form = ProductCommentForm()
    return render(request, 'add_comment.html', {'form': form, 'product': product})

@login_required(login_url='accounts:login')
def delete_comment(request, product_id):
    comment = get_object_or_404(ProductComment, id=product_id)
    if request.method == 'DELETE':
        if comment.user == request.user:
            comment.delete()
            

            return redirect(request.path)

@login_required(login_url='accounts:login')
def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES['image']

        product = Product.objects.create(
            name=name,
            price=price,
            description=description,
            image=image
        )

        return redirect('products')

    return render(request, 'products/add_product.html')

@login_required(login_url='accounts:login')
def edit_product(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.description = request.POST['description']
        product.image = request.FILES['image']

        product.save()

        return redirect('products:home')

    return render(request, 'products/edit_product.html', context={'product': product})

@login_required(login_url='accounts:login')
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()

    return redirect('products')