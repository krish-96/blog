from django.contrib import admin
from .models import ContactUs
from import_export.admin import ImportExportModelAdmin

@admin.register(ContactUs)
class ContactUsAdmin(ImportExportModelAdmin):
    list_display = ['name', 'email', 'subject', 'body']

# Register your models here.

# admin.site.register(ContactUs, ContactUsAdmin)