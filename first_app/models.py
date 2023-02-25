from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    Drafted = 'd'
    Published = 'p'
    STATUS_CHOICES = [
        ( Drafted,'در انتظار'),
        (Published , 'منتشر شده')
    ]
    title = models.CharField(max_length=200,verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length = 200, unique=True,verbose_name="آدرس")
    description = models.TextField(verbose_name="محتوا")
    thumbnail = models.ImageField(upload_to="pics")
    published_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES,max_length=1,default='d',verbose_name="وضعیت")
    category = models.ManyToManyField('Category',verbose_name="دسته بندی")
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله" 

    def save(self, *args ,**kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)   
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=256,verbose_name="عنوان")
    slug =models.SlugField(unique=True,verbose_name="آدرس")
    status = models.BooleanField(default=False,verbose_name = "آیا تایید شده هست؟")
    position = models.IntegerField(verbose_name="جایگاه")
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural =" دسته بندی ها"
        ordering = ['position']
        
    def __str__(self):
        return self.title