from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Author, Post, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("post_author", "post_tag", "post_date")
    list_display = ("post_title", "post_author", "post_date")
    prepopulated_fields = {
        "post_slug": ("post_title",)
    }


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
