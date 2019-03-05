from django.contrib import admin
from .models import DNAStrings

# Register your models here.
@admin.register(DNAStrings)
class DNAStringsAdmin(admin.ModelAdmin):
    pass