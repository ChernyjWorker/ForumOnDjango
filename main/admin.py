from django.contrib import admin
from .models import Category, Post, Commentary

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('created_at','title','content','category','updated_at')
    list_display_links = ('title','content')
    search_fields = ('title', 'content', 'created_at')
    
    
    prepopulated_fields = {
        'slug' : ('title',)
    }
    
    
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ('user','post','content','created_at','updated_at')
    list_display_links = ('content','post','user')
    search_fields = ('user', 'post', 'content')
    
    readonly_fields = ('user', 'post', 'content')
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    
    prepopulated_fields = {
        'slug': ('name',)
    }
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Commentary, CommentaryAdmin)
