from django.db import models
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    
    name = models.CharField(max_length=100, verbose_name='Имя')
    slug = models.SlugField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ('name',)
        
        
class Post(models.Model):
    
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100)
    content = models.TextField(verbose_name='Контент поста')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Дата последнего обновления')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'
        ordering = ('title','created_at','updated_at')

