from django.shortcuts import render
form .models import Equipments

# Create your views here.
@login_required
def equipments(request):
    equipments = Equipments
    context = {}

@login_required
def areas(request):
    pass