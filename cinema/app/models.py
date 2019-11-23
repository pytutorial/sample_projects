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

class Movie(models.Model):
    class Status:
        CURRENT = 1
        UPCOMING = 2

    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=200, verbose_name='Tên')        
    description = models.CharField(max_length=500, blank=True)
    category = models.ForeignKey(Category, verbose_name='Thể loại', on_delete=models.PROTECT)
    language = models.ForeignKey(Language, verbose_name='Ngôn ngữ', on_delete=models.PROTECT)
    duration = models.IntegerField(verbose_name='Thời lượng (phút)')
    onDate = models.DateField(blank=False, null=False, verbose_name='Ngày khởi chiếu')
    price = models.IntegerField(verbose_name='Giá vé (₫)')
    upcoming = models.BooleanField(verbose_name='Chưa khởi chiếu')
    image = models.ImageField(upload_to='static/images', verbose_name='Ảnh giới thiệu')  

    def __str__(self):
        return self.name

class MovieShow(models.Model):
    movie = models.ForeignKey(Movie, verbose_name="Phim", on_delete=models.PROTECT)
    dayOfWeek = models.IntegerField(verbose_name="Ngày trong tuần", 
                            help_text="Chủ nhật:1, Thứ 2: 2, ..., Thứ 7: 7")
    time = models.TimeField(verbose_name="Giờ chiếu", help_text="Thời gian dạng HH:mm")
    room = models.CharField(max_length=30, verbose_name="Phòng chiếu")