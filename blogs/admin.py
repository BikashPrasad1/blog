from django.contrib import admin
from .models import Category
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'category', 'status', 'created_at','is_featured')
    search_fields = ('id', 'title', 'author__username', 'category__category_name', 'status')
    list_editable = ('status', 'is_featured')

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
