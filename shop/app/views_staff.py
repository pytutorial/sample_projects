from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms_staff import *
from datetime import datetime

#================================== Manage products ========================================

@login_required
def listProduct(request):
    products = Product.objects.all()    
    return render(request, 'staff/product/list.html', {'products': products})

@login_required
def createProduct(request):
    form = ProductForm()
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product-list')
        
    return render(request, 'staff/product/form.html', {'form': form})

@login_required
def updateProduct(request, id):
    p = get_object_or_404(Product, pk=id)
    form = ProductForm(instance=p)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            return redirect('product-list')
        
    return render(request, 'staff/product/form.html', {'form': form})

@login_required
def deleteProduct(request, id):
    p = get_object_or_404(Product, pk=id)
    p.delete()
    return redirect('product-list')

#================================== Manage orders ========================================
@login_required 
def listOrder(request):
    orders = Order.objects.all().order_by('status')
    return render(request, 'staff/order/list.html', {'orders': orders})

@login_required 
def deliverOrder(request, id):
    deliverDate_error = ''
    if request.method == 'POST':
        try:
            deliverDate = datetime.strptime(request.POST['deliverDate'], '%d/%m/%Y %H:%M')
        except:
            deliverDate_error = 'Thời gian không hợp lệ'
        
        if deliverDate_error == '':
            order = get_object_or_404(Order, pk=id)
            order.status = Order.Status.DELIVERED
            order.deliverDate = deliverDate
            order.save()
            return redirect('order-list')
    
    return render(request, 'staff/order/deliver_form.html', {'deliverDate_error' : deliverDate_error})

@login_required 
def cancelOrder(request, id):
    order = get_object_or_404(Order, pk=id)
    order.status = Order.Status.CANCELED
    order.save()
    return redirect('order-list')

#================================== Manage manufacturers ========================================
@login_required
def listManufacturer(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, 'staff/manufacturer/list.html', {'manufacturers': manufacturers})

@login_required
def createManufacturer(request):
    form = ManufacturerForm()
    
    if request.method == 'POST':
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manufacturer-list')

    return render(request, 'staff/manufacturer/form.html', {'form': form})

@login_required
def updateManufacturer(request, id):
    m = get_object_or_404(Manufacturer, pk=id)
    form = ManufacturerForm(instance=m)
    
    if request.method == 'POST':
        form = ManufacturerForm(request.POST, instance=m)
        if form.is_valid():
            form.save()
            return redirect('manufacturer-list')

    return render(request, 'staff/manufacturer/form.html', {'form': form})

@login_required
def deleteManufacturer(request, id):
    m = get_object_or_404(Manufacturer, pk=id)
    m.delete()
    return redirect('manufacturer-list')    


#================================== Manage cpu types ========================================
@login_required
def listCpuType(request):
    cpuTypes = CpuType.objects.all()
    return render(request, 'staff/cpu_type/list.html', {'cpuTypes': cpuTypes})

@login_required
def createCpuType(request):
    form = CpuTypeForm()

    if request.method == 'POST':
        form = CpuTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cpu-type-list')

    return render(request, 'staff/cpu_type/form.html', {'form': form})

@login_required
def updateCpuType(request, id):
    cpuType = get_object_or_404(CpuType, pk=id)
    form = CpuTypeForm(instance=cpuType)

    if request.method == 'POST':
        form = CpuTypeForm(request.POST, instance=cpuType)
        if form.is_valid():
            form.save()
            return redirect('cpu-type-list')

    return render(request, 'staff/cpu_type/form.html', {'form': form})

@login_required
def deleteCpuType(request, id):
    cpuType = get_object_or_404(CpuType, pk=id)
    cpuType.delete()
    return redirect('cpu-type-list')

#================================== Manage disk types ========================================
@login_required
def listDiskType(request):
    diskTypes = DiskType.objects.all()
    return render(request, 'staff/disk_type/list.html', {'diskTypes': diskTypes})

@login_required
def createDiskType(request):
    form = DiskTypeForm()

    if request.method == 'POST':
        form = DiskTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disk-type-list')

    return render(request, 'staff/disk_type/form.html', {'form': form})

@login_required
def updateDiskType(request, id):
    diskType = get_object_or_404(DiskType, pk=id)
    form = DiskTypeForm(instance=diskType)

    if request.method == 'POST':
        form = DiskTypeForm(request.POST, instance=diskType)
        if form.is_valid():
            form.save()
            return redirect('disk-type-list')

    return render(request, 'staff/disk_type/form.html', {'form': form})

@login_required
def deleteDiskType(request, id):
    diskType = get_object_or_404(DiskType, pk=id)
    diskType.delete()
    return redirect('disk-type-list')