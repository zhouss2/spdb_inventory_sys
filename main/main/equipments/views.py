from django.shortcuts import render
from .models import Equipment
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def equipments(request):
    equipments = Equipment.objects.all()
    context = {'equipments':equipments}
    return render


@login_required
def areas(request):
    pass