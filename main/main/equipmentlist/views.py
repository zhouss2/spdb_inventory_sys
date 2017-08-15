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
        equipment_list = []
        for x in context['object_filter']:
            equipment_list.append(x.equipment.name)
        o_all = Operation.objects.all().order_by('date_time')
        dict_date = {}
        for o in o_all:
            if o.date_time in dict_date:
                i = equipment_list.index(o.equipment.name)
                dict_date[o.date_time][i] = o.status + '-' + str(o.quantity)
            else:
                dict_date[o.date_time] = [0 for x in range(len(equipment_list))]
                i = equipment_list.index(o.equipment.name)
                dict_date[o.date_time][i] = o.status + '-' + str(o.quantity)
        context['dict_date'] = dict_date
        # context['object_date_time'] = Operation.objects.distinct('date_time').order_by('date_time')
        return context


def equipmentareaidles(request):
    equipmentareaidles = EquipmentAreaIdle.objects.all()
    module_dict = {}
    for equipmentareaidle in equipmentareaidles:
        name = equipmentareaidle.area.name
        equipmentname = equipmentareaidle.equipment.name
        if name in module_dict:
            module_dict[name].append([equipmentname, equipmentareaidle.idle_quantity])
        else:
            module_dict[name] = [[equipmentname, equipmentareaidle.idle_quantity]]
    return render(request, 'equipments/equipmentareaidle.html', {'module_dict':module_dict,'Dict': json.dumps(module_dict)})
