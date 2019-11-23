from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.fullname

class Author(models.Model):    
    name = models.CharField(max_length=50, verbose_name='Tên', unique=True)
    country = models.CharField(max_length=30, verbose_name="Quốc gia")

    def __str__(self):
        return self.name

class Publisher(models.Model):
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=30, verbose_name='Tên')

    def __str__(self):
        return self.name

class Category(models.Model):
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=30, verbose_name='Tên')

    def __str__(self):
        return self.name
    
class Book(models.Model):
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    title = models.CharField(max_length=200, verbose_name='Tiêu đề')
    description = models.CharField(max_length=500, blank=True)
    category = models.ForeignKey(Category, verbose_name="Thể loại",  on_delete=models.PROTECT)
    author = models.ForeignKey(Author, verbose_name="Tác giả", on_delete=models.PROTECT)
    publisher = models.ForeignKey(Publisher, verbose_name="Nhà xuất bản", on_delete=models.PROTECT)
    publishYear = models.IntegerField(verbose_name="Năm xuất bản")
    numberOfPage = models.IntegerField(verbose_name="Số trang")    
    numberOfCopy = models.IntegerField(verbose_name="Số bản copy")
    numberOfAvailableCopy = models.IntegerField(blank=True)
    image = models.ImageField(verbose_name='Ảnh bìa', upload_to='static/images')

    def __str__(self):
        return self.title

class BookRent(models.Model):
    class Status:
        PENDING = 0
        BORROWING = 1
        RETURNED = 2

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField()
    startDate = models.DateField()
    dueDate = models.DateField()
    returnDate = models.DateField(blank=True, null=True)