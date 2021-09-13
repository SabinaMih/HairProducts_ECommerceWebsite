from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Review, Voucher
from .forms import ReviewForm, VoucherApplyForm
from django.core.paginator import Paginator, EmptyPage, InvalidPage 
from django.utils import timezone
from django.views.decorators.http import require_POST


def allProductCategories(request, category_id=None):
    c_page = None
    products_list = None
    if category_id != None:
        c_page = get_object_or_404(Category, id=category_id)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    
    '''Paginator code'''
    paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)    
    return render(request, 'shop/category.html', {'category':c_page, 'products':products})

def product_details(request, category_id, product_id):
    try:
        product = Product.objects.get(category_id=category_id, id=product_id)
    except Exception as e:
        raise e
    return render(request, 'shop/product.html', {'product':product})

# function for our reviews
def add_review_to_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.author = request.user
            review.save()
            return redirect('shop:allProductCategories')
    else:
        form = ReviewForm()
    return render(request, 'add_review_to_product.html', {'form':form})


@require_POST
def voucher_apply(request):
    now = timezone.now()
    form = VoucherApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            voucher = Voucher.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            request.session['voucher_id'] = voucher.id 
        except Voucher.DoesNotExist:
            request.session['voucher_id'] = None
    return redirect('cart:cart_detail')