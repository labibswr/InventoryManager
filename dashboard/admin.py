from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.site_header = 'InvenMgmt Admin Panel'

# Display inventory as table
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']
    list_filter = ['category']

# Register your models here.
admin.site.register(Item, ProductAdmin)
admin.site.register(Loan)
