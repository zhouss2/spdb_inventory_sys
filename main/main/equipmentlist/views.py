from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone
from main.equipments.models import EquipmentArea, Operation, EquipmentAreaIdle
import json

# Create your views here.
class EquipmentListView(ListView):
    model = EquipmentArea
 
    def get_context_data(self, **kwargs):
        context = super(EquipmentListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


# Create your views here.
class OperationListView(ListView):
    model = Operation
 
    def get_context_data(self, **kwargs):
        context = super(OperationListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['object_filter'] = Operation.objects.distinct('equipment')
        context['object_date_time'] = Operation.objects.order_by('date_time')
        return context


def equipmentareaidles(request):
    equipmentareaidles = EquipmentAreaIdle.objects.all()
    module_dict = {}
    for equipmentareaidle in equipmentareaidles:
        name = equipmentareaidle.equipment_area.area.name
        equipmentname = equipmentareaidle.equipment_area.equipment.name
        if name in module_dict:
            module_dict[name].append([equipmentname, equipmentareaidle.idle_quantity])
        else:
            module_dict[name] = [[equipmentname, equipmentareaidle.idle_quantity]]
    return render(request, 'equipments/equipmentareaidle.html', {'module_dict':module_dict,'Dict': json.dumps(module_dict)})
