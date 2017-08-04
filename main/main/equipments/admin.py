from django.contrib import admin

from .models import EquipmentType,Equipment, Area, EquipmentArea, Operation

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

    class Meta:
        model = Operation
        
admin.site.register(Operation, OperationAdmin)
admin.site.register(EquipmentType)
admin.site.register(Area)
admin.site.register(EquipmentArea)
admin.site.register(Equipment, EquipmentAdmin)
