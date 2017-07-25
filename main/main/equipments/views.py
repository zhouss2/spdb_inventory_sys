from django.shortcuts import render
from .models import Equipment
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
# Create your views here.
# 
# 
@cache_page(60 * 15)
@login_required
def equipments(request):
    equipments = Equipment.objects.all()
    return render(request, 'core/network.html', equipments)


@login_required
def areas(request):
    pass

