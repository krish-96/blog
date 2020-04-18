from django.contrib import admin
from .models import ContactUs, Author, Post
from import_export.admin import ImportExportModelAdmin

@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ['name', 'dob', 'phone_no', 'email', 'address', 'slug', 'photo', 'joined_date']

@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    list_display = ['title', 'creator', 'content', 'post_pic', 'slug', 'privacy', 'status', 'created_date', 'updated_date', 'published_date']

@admin.register(ContactUs)
class ContactUsAdmin(ImportExportModelAdmin):
    list_display = ['name', 'email', 'subject', 'body']
