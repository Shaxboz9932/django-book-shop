from django.contrib import admin
from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title')

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
