from django.contrib import admin
from .models import Patient, File

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("full_name",)}
    list_display = ("full_name",)


# class FileAdmin(admin.ModelAdmin):
   
#     list_display = ("user_file", "patient",)

admin.site.register(Patient, PatientAdmin)
admin.site.register(File)