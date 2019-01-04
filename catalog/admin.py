from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(BookInstance)

#define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass

#Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)    

# Register the Admin classes for Book using the decorator (this does exactly the same thing as the admin.site.register() syntax):
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.rergister(BookInstance)
class BookInstanceAdmin(admmin.ModelAdmin)
    pass