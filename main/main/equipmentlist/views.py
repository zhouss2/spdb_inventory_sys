from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone
from main.equipments.models import EquipmentArea, Operation


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

