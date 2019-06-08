from django.contrib import admin;
from bins.models import Bin;
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class BinViewCustomization(ImportExportModelAdmin,admin.ModelAdmin):
    """
    we inherit from ImportExportModelAdmin to allow third package part import_export to work within admin

    also we inherit from admin.ModelAdmin to custimz view of Bin in Admin
    """
    list_display=('pk','title','language','author','created','updated');
    list_filter=('author',)
    ordering=('-created',);
    date_hierarchy = 'created'
admin.site.register(Bin,BinViewCustomization);