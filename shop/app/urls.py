from django.urls import path, include
from . import views, views_user, views_staff

urlpatterns =[
    # ================================= Log in ============================================
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup), 

    # ================================Customer pages =========================================
    path('', views_user.home, name='home'),
    path('promotions', views_user.promotions, name='promotions'),
    path('contact', views_user.contact, name='contact'),
    path('product_detail/<int:id>', views_user.viewProduct, name='view-product'),
    path('purchase/<int:id>', views_user.purchase, name='purchase'),
    path('purchase_confirm/<int:id>', views_user.purchaseConfirm, name='purchase-confirm'),
    path('thank_you', views_user.thankYou, name='thank-you'),  

    # ================================Staff pages =========================================

    # Manage products
    path('staff', views_staff.listProduct, name='product-list'),
    path('staff/product_create', views_staff.createProduct, name='product-create'),  
    path('staff/product_update/<int:id>', views_staff.updateProduct, name='product-update'),  
    path('staff/product_delete/<int:id>', views_staff.deleteProduct, name='product-delete'),  

    # Manage manufactures
    path('staff/manufacturer_list', views_staff.listManufacturer, name='manufacturer-list'),  
    path('staff/manufacturer_create', views_staff.createManufacturer, name='manufacturer-create'),  
    path('staff/manufacturer_update/<int:id>', views_staff.updateManufacturer, name='manufacturer-update'),  
    path('staff/manufacturer_delete/<int:id>', views_staff.deleteManufacturer, name='manufacturer-delete'),  
    
    # Manage cpu types
    path('staff/cpu_type_list', views_staff.listCpuType, name='cpu-type-list'),  
    path('staff/cpu_type_create', views_staff.createCpuType, name='cpu-type-create'),  
    path('staff/cpu_type_update/<int:id>', views_staff.updateCpuType, name='cpu-type-update'),  
    path('staff/cpu_type_delete/<int:id>', views_staff.deleteCpuType, name='cpu-type-delete'),  

    # Manage disk types
    path('staff/disk_type_list', views_staff.listDiskType, name='disk-type-list'),  
    path('staff/disk_type_create', views_staff.createDiskType, name='disk-type-create'),  
    path('staff/disk_type_update/<int:id>', views_staff.updateDiskType, name='disk-type-update'),  
    path('staff/disk_type_delete/<int:id>', views_staff.deleteDiskType, name='disk-type-delete'),      
]