from django.contrib import admin
from .models import Banks
# Register your models here.
from import_export.admin import ImportExportModelAdmin

@admin.register(Banks)
class ViewAdmin(ImportExportModelAdmin):
    pass