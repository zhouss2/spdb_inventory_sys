from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main.equipments.models import EquipmentArea, Equipment
from main.questions.models import Question
from main.feeds.models import Feed
from django.contrib.auth.models import User

import json
# Create your views here.
# 
# 
def overview(request):
    equipments = EquipmentArea.objects.all()
    questions = len(Question.get_unanswered())
    users = len(User.objects.filter(is_active=True))
    equipment_quantity = len(Equipment.objects.all())
    feed = len(Feed.get_feeds())
    module_dict = {}
    for equipment in equipments:
        if equipment.area.name in module_dict:
            module_dict[equipment.area.name].append([equipment.equipment.name, equipment.quantity])
        else:
            module_dict[equipment.area.name] = [[equipment.equipment.name, equipment.quantity]]
    # print(module_dict)
    return render(request, 'overview.html', {'module_dict':module_dict,'Dict': json.dumps(module_dict),
        'undone_questions':questions,'active_users':users,'equipment_quantity':equipment_quantity,'feed':feed})