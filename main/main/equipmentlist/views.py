from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone
from main.equipments.models import Equipment


# Create your views here.
class EquipmentListView(ListView):
    model = Equipment
 
    def get_context_data(self, **kwargs):
        context = super(EquipmentListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

