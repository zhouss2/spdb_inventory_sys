from __future__ import absolute_import

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Area(models.Model):
    """docstring for ClassName"""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'
        ordering = ('-update_date',)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class EquipmentType(models.Model):
    """docstring for ClassName"""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'EquipmentType'
        verbose_name_plural = 'EquipmentTypes'
        ordering = ('-update_date',)
        
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Equipment(models.Model):
    """docstring for ClassName"""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    # quantity = models.IntegerField(default=0)
    update_date = models.DateTimeField(auto_now_add=True)
    # area = models.ForeignKey(Area)
    equipment_type = models.ForeignKey(EquipmentType, default=0)
    # is_wasted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'
        ordering = ('-update_date',)
        
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_quantity(self):
        return sum([x.quantity for x in EquipmentArea.objects.filter(equipment=self)])


class EquipmentArea(models.Model):
    """docstring for ClassName"""
    area = models.ForeignKey(Area)
    equipment = models.ForeignKey(Equipment)
    quantity = models.IntegerField(default=0)


    class Meta:
        verbose_name = 'EquipmentArea'
        verbose_name_plural = 'EquipmentAreas'

    def __str__(self):
        return self.equipment.name

    def __unicode__(self):
        return self.equipment.name

class Operation(models.Model):
    """docstring for ClassName"""
    IN = 'I'
    WASTED = 'W'
    TRANSFER = 'T'
    STATUS = (
        (IN, 'IN'),
        (WASTED, 'WASTED'),
        (TRANSFER, 'TRANSFER'),
    )
    equipment = models.ForeignKey(Equipment)
    status = models.CharField(max_length=1, choices=STATUS, default=IN)
    quantity = models.IntegerField(default=0)
    date_time = models.DateTimeField()
    remark = models.TextField(max_length=2000, blank=True, null=True)

    class Meta:
            verbose_name = 'Operation'
            verbose_name_plural = 'Operations'
     
    def __str__(self):
        return self.equipment.name

    def __unicode__(self):
        return self.equipment.name         