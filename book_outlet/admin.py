from django.contrib import admin
from .models import Book, Author, Address, Country



@admin.register(Book)      
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author", "rating",)

admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")

admin.site.register(Address)
# class AdminAdress(admin.ModelAdmin):

admin.site.register(Country)

