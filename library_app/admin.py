from django.contrib import admin
from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
    """
    Admin view for the Book model. Defines how books are displayed in the admin panel.
    """
    list_display = ('title', 'genre', 'publication_date', 'availability_status', 'user')
    list_filter = ('genre', 'availability_status', 'publication_date')
    search_fields = ('title', 'genre')

class AuthorAdmin(admin.ModelAdmin):
    """
    Admin view for the Author model. Defines how authors are displayed in the admin panel.
    """
    list_display = ('name', 'birth_date', 'user')
    list_filter = ('birth_date',)
    search_fields = ('name', 'bio')

# Registering the models with their respective custom admin classes
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
