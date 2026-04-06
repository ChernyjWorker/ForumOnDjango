from django.db import models

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100)
    content = models.TextField(verbose_name='Контент поста')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True, verbose_name = 'Дата последнего обновления')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'
        ordering = ('title','created_at','updated_at')
        