from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    
    list_display = ('created_at','title','content','updated_at')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', 'created_at')
    
    
    prepopulated_fields = {
        'slug' : ('title',)
    }
    
admin.site.register(Post, PostAdmin)