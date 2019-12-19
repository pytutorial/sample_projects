from django.db import models

class Manufacturer(models.Model):
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=30, verbose_name='Tên')

    def __str__(self):
        return self.name

class CpuType(models.Model):
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=30, verbose_name='Tên')

    def __str__(self):
        return self.name

class DiskType(models.Model):
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=30, verbose_name='Tên')

    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=100, verbose_name='Tên')
    description = models.CharField(max_length=500, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name='Hãng sản xuất', on_delete=models.PROTECT)
    
    cpu = models.CharField(max_length=30)
    cpuType = models.ForeignKey(CpuType, verbose_name='Loại CPU', on_delete=models.PROTECT)

    ramSize = models.FloatField(verbose_name='Dung lượng RAM (GB)')
    
    diskSize = models.FloatField(verbose_name='Dung lượng ổ cứng (GB)')
    diskType = models.ForeignKey(DiskType, verbose_name='Loại ổ cứng', on_delete=models.PROTECT)

    screenSize = models.FloatField(verbose_name='Kích thước màn hình (inch)')
    weight = models.FloatField(verbose_name='Khối lượng (kg)')
    price = models.IntegerField(verbose_name='Giá (₫)')
    image = models.ImageField(verbose_name='Ảnh sản phẩm', upload_to='static/images')

    def __str__(self):
        return self.name

class Order(models.Model):
    class Status:
        ORDERED = 1
        DELIVERED = 2
        CANCELED = 3
        
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    orderDate = models.DateTimeField()
    deliverDate = models.DateTimeField(null=True)
    status = models.IntegerField()