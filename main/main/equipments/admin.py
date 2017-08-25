from django.contrib import admin

from .models import EquipmentType,Equipment, Area, EquipmentArea, Operation, EquipmentAreaIdle

# -*- coding: utf-8 -*-
# Register your models here.

class EquipmentAdmin(admin.ModelAdmin):
    """docstring for ClassName"""
    prepopulated_fields = {"description": ("name",)}
    list_display = ('name', 'description')

    # def view_quantity(self, obj):
    #     return sum([x.quantity for x in obj.objects.filter(equipment=obj)])

    class Meta:
        model = Equipment


class OperationAdmin(admin.ModelAdmin):
    """docstring for ClassName"""
    list_display = ('equipment', 'status', 'quantity', 'date_time')
    search_fields = ['equipment__name', 'status', 'date_time']
    class Meta:
        model = Operation

class EquipmentAreaAdmin(admin.ModelAdmin):
    """docstring for ClassName"""
    list_display = ('equipment', 'area', 'quantity')
    search_fields = ['area__name', 'equipment__name']
    class Meta:
        model = EquipmentArea

class EquipmentAreaIdleAdmin(admin.ModelAdmin):
    """docstring for ClassName"""
    list_display = ('equipment', 'area', 'idle_quantity')
    search_fields = ['area__name', 'equipment__name']
    class Meta:
        model = EquipmentAreaIdle
        
admin.site.register(Operation, OperationAdmin)
admin.site.register(EquipmentType)
admin.site.register(Area)
admin.site.register(EquipmentArea, EquipmentAreaAdmin)
admin.site.register(EquipmentAreaIdle,EquipmentAreaIdleAdmin)
admin.site.register(Equipment, EquipmentAdmin)
