from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=66, unique=True)
    avatar = models.ImageField(upload_to='avatars/',blank=True,null=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.username+'|'+self.email
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'
        