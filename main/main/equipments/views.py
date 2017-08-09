from django.shortcuts import render
from .models import Equipment, Operation, EquipmentArea, EquipmentAreaIdle
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.views.generic.list import ListView
from django.utils import timezone

# Create your views here.
# 
# 
@cache_page(60 * 15)
@login_required
def equipments(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment/equipments.html', {'equipments': equipments})


@login_required
def areas(request):
    pass


@login_required
def operations(request):
    operations = Operation.objects.orderby("date_time")
    equipment = Equipment.objects.all()


    return render(request, 'equipment/operations.html', {'operations': operations})

