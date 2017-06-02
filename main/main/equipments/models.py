from __future__ import absolute_import

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Area(models.Model):
    """docstring for ClassName"""
    name = models.CharField(max_length=255)
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


class Equipment(models.Model):
    """docstring for ClassName"""
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    update_date = models.DateTimeField(auto_now_add=True)
    area = models.ForeignKey(Area)



    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'
        ordering = ('-update_date',)
        
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name



