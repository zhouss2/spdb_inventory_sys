from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone
from main.equipments.models import EquipmentArea, Operation, EquipmentAreaIdle, Area, EquipmentType,Equipment
import json
from django.db.models import Q 
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



def equipmentlistbyarea(request):
    areas = Area.objects.filter(~Q(name='warehouse'))
    module_dict = {}
    for e in areas:
        name = e.name
        if name in module_dict:
            pass
        else:
            module_dict[name] = sum([x.quantity for x in EquipmentArea.objects.filter(area=e)])
    return render(request, 'equipments/equipmentlistbyarea.html', {'module_dict':module_dict})


def equipmentlistbylcd(request):
    et = EquipmentType.objects.filter(pk=1) # lcd
    equipment = Equipment.objects.filter(~Q(equipment_type=et))
    areas = Area.objects.filter(~Q(name='warehouse'))

    module_dict = {}
    len_module = 0
    for a in areas:
        name = a.name
        if name in module_dict:
            pass
        else:
            module_dict[name] = []
            for e in equipment:
                ea = EquipmentArea.objects.filter(area=a, equipment=e)
                num = 0
                if len(ea) > 0:
                    num = ea[0].quantity
                module_dict[name].append(num)
            len_module = len(module_dict[name])
    module_dict[u'总计'] = [0 for x in range(len_module)]
    for k,v in module_dict.items():
        if k!=u'总计':
            for i,value in enumerate(v):
                module_dict[u'总计'][i] += value
    return render(request, 'equipments/equipmentlistbylcd.html', {'module_dict':module_dict,'equipment':equipment})


def equipmentlistbypc(request):
    et = EquipmentType.objects.filter(pk=2) # pc
    equipment = Equipment.objects.filter(~Q(equipment_type=et))
    areas = Area.objects.filter(~Q(name='warehouse'))

    module_dict = {}
    len_module = 0
    for a in areas:
        name = a.name
        if name in module_dict:
            pass
        else:
            module_dict[name] = []
            for e in equipment:
                ea = EquipmentArea.objects.filter(area=a, equipment=e)
                num = 0
                if len(ea) > 0:
                    num = ea[0].quantity
                module_dict[name].append(num)
            len_module = len(module_dict[name])
    module_dict[u'总计'] = [0 for x in range(len_module)]
    for k,v in module_dict.items():
        if k!=u'总计':
            for i,value in enumerate(v):
                module_dict[u'总计'][i] += value
    return render(request, 'equipments/equipmentlistbypc.html', {'module_dict':module_dict,'equipment':equipment})
