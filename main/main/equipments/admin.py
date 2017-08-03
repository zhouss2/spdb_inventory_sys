from django.contrib import admin

from .models import EquipmentType,Equipment, Area, EquipmentArea

# -*- coding: utf-8 -*-
# Register your models here.

# class EquipmentAdmin(admin.ModelAdmin):
#     """docstring for ClassName"""
#     prepopulated_fields = {"description": ("name",)}
#     list_display = ('name', 'quantity', 'description')

#     class Meta:
#         model = Equipment
        

admin.site.register(EquipmentType)
admin.site.register(Area)
admin.site.register(EquipmentArea)
admin.site.register(Equipment)
