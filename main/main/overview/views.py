from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main.equipments.models import Equipment
import json
# Create your views here.
# 
# 
def overview(request):
    equipments = Equipment.objects.all()
    module_dict = {}
    for equipment in equipments:
        if equipment.area.name in module_dict:
            module_dict[equipment.area.name].append([equipment.name, equipment.quantity])
        else:
            module_dict[equipment.area.name] = [[equipment.name, equipment.quantity]]
    return render(request, 'overview.html', {'module_dict':module_dict,'Dict': json.dumps(module_dict)})