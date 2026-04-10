from django import forms
from django.utils.text import slugify

from .models import Post

class CreatePostForm(forms.ModelForm):
    
    title = forms.CharField(label='Заголовок поста', required=True)
    slug = forms.SlugField(required=False, widget=forms.HiddenInput())
    content = forms.Textarea()
    
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        if not instance.slug:
            instance.slug = slugify(instance.title, allow_unicode=True)
        if commit:
            instance.save()
        return instance
    
    
    class Meta:
        model = Post
        
        fields = ('title', 'slug', 'content')
