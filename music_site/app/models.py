from django.db import models

class Language(models.Model):
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=50, verbose_name='Tên')

    def __str__(self):
        return self.name

class Category(models.Model):
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=50, verbose_name='Tên')

    def __str__(self):
        return self.name

class Author(models.Model):    
    name = models.CharField(max_length=50, verbose_name='Tên', unique=True)
    country = models.CharField(max_length=30, verbose_name="Quốc gia")

    def __str__(self):
        return self.name

class Artist(models.Model):    
    name = models.CharField(max_length=50, verbose_name='Tên', unique=True)
    country = models.CharField(max_length=30, verbose_name="Quốc gia")

    def __str__(self):
        return self.name

class Song(models.Model):
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    title = models.CharField(max_length=200, verbose_name='Tiêu đề')
    description = models.CharField(max_length=500, blank=True)
    category = models.ForeignKey(Category, verbose_name="Thể loại",  on_delete=models.PROTECT)
    language = models.ForeignKey(Language, verbose_name='Ngôn ngữ', on_delete=models.PROTECT)
    artist = models.ForeignKey(Artist, verbose_name="Ca sĩ thể hiện", on_delete=models.PROTECT)
    author = models.ForeignKey(Author, verbose_name="Nhạc sĩ sáng tác", on_delete=models.PROTECT)
    releaseYear = models.IntegerField(verbose_name="Năm phát hành", blank=True, null=True)
    file = models.FileField(upload_to='static/music', verbose_name='File nhạc')  

    def __str__(self):
        return self.title
