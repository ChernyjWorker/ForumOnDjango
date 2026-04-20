from django import forms
from django.utils.text import slugify
from transliterate import translit

from .models import Category, Post, Commentary

class CreatePostForm(forms.ModelForm):
    
    category = forms.ModelChoiceField(queryset=Category.objects.all(), 
                                        required=True, label = 'Категория поста')
    title = forms.CharField(label='Заголовок поста', required=True)
    slug = forms.SlugField(required=False, widget=forms.HiddenInput())
    content = forms.Textarea()
    
    
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        translit_title = translit(instance.title, 'ru',reversed=True)
        
        if not instance.slug:
            instance.slug = slugify(f'post-{translit_title}')
        if commit:
            instance.save()
        return instance
    
    
    class Meta:
        model = Post
        
        fields = ('category','title', 'slug', 'content')
        
        
class CreateCommentaryForm(forms.ModelForm):
    content = forms.Textarea(attrs={'class':'form-control', 'placeholder':'Оставьте свой отзыв...', 'rows':'5'})
    
    class Meta:
        model = Commentary
        fields = ('content',)
        
        
