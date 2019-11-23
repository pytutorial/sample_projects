from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms_user import *

priceRanges = [
    {'min': 0, 'max': 10, 'label': 'Dưới 10 triệu'},
    {'min': 10, 'max': 15, 'label': 'Từ 10 đến 15 triệu'},
    {'min': 15, 'max': 20, 'label': 'Từ 15 đến 20 triệu'},
    {'min': 20,  'label': 'Trên 20 triệu'}    
]

def home(request):
    queryParams = request.GET
    productName = queryParams.get('product_name')
    manufacturerId = queryParams.get('manufacturer_id')
    priceRange = queryParams.get('price_range')
    cpuTypeId = queryParams.get('cpu_type_id')
    ramSize = queryParams.get('ram_size')
    diskTypeId = queryParams.get('disk_type_id')    

    products = Product.objects.all()
    
    if productName:
        products = products.filter(name__contains=productName)

    if manufacturerId:
        products = products.filter(manufacturer=Manufacturer.objects.get(id=manufacturerId))

    if priceRange:
        priceRange = priceRanges[int(priceRange)-1]
        minPrice = priceRange.get('min')
        maxPrice = priceRange.get('max')
        
        if minPrice:
            products = products.filter(price__gte=minPrice*1000000)
        
        if maxPrice:
            products = products.filter(price__lte=maxPrice*1000000)

    if ramSize:
        products = products.filter(ramSize=ramSize)

    if cpuTypeId:
        products = products.filter(cpuType=CpuType.objects.get(id=cpuTypeId))

    if diskTypeId:
        products = products.filter(diskType=DiskType.objects.get(id=diskTypeId))

    context=  {
        'queryParams': queryParams,
        'products': products,
        'priceRanges': priceRanges,
        'manufacturers': Manufacturer.objects.all(),
        'cpuTypes': CpuType.objects.all(),
        'diskTypes': DiskType.objects.all()
    }

    return render(request, 'user/index.html', context)

def promotions(request):
    return render(request, 'user/promotions.html', {'page': 1})

def contact(request):
    return render(request, 'user/contact.html', {'page': 2})

def viewProduct(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'user/view_product.html', {'product': product})

def purchase(request, id):
    product = get_object_or_404(Product, pk=id)
    form = PurchaseForm()
    
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        
        if form.is_valid():
            request.session['purchase_form'] = form.cleaned_data
            return redirect('purchase-confirm', id)

    return render(request, 'user/purchase.html', {'product': product, 'form': form})

def purchaseConfirm(request, id):
    product = get_object_or_404(Product, pk=id)
    form = request.session.get('purchase_form')
    return render(request, 'user/purchase_confirmation.html', {'product': product, 'form': form})

def thankYou(request):
    return render(request, 'user/thank_you.html')
