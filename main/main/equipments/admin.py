from django.contrib import admin

from .models import Equipment, Area

# -*- coding: utf-8 -*-
# Register your models here.

class EquipmentAdmin(admin.ModelAdmin):
    """docstring for ClassName"""
    prepopulated_fields = {"description": ("name",)}
    list_display = ('area', 'name', 'quantity', 'description')

    class Meta:
        model = Equipment
        


admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Area)