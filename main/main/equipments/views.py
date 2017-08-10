from django.shortcuts import render
from .models import Equipment, Operation, EquipmentArea, EquipmentAreaIdle, EquipmentType, Area
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.views.generic.list import ListView
from django.utils import timezone
import xlrd
import uuid
import random

# Create your views here.
# 
# 
@cache_page(60 * 15)
@login_required
def equipments(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment/equipments.html', {'equipments': equipments})


@login_required
def areas(request):
    pass


@login_required
def operations(request):
    operations = Operation.objects.orderby("date_time")
    equipment = Equipment.objects.all()


    return render(request, 'equipment/operations.html', {'operations': operations})

def excel_table_by_name(file_excel=r'xls/lcd.xlsx',
                        col_name_index=0, by_name=u'Sheet1'):
    """
        根据名称获取Excel表格中的数据
        参数: file_excel：Excel文件路径
             col_name_index：表头列名所在行的所以
             by_name：Sheet1名称
    """
    data = xlrd.open_workbook(file_excel)
    table = data.sheet_by_name(by_name)
    n_rows = table.nrows   # 行数
    col_names = table.row_values(col_name_index)  # 某一行数据
    # row_dict = {}
    # for row_num in range(1, n_rows):
    #     row = table.row_values(row_num)
    #     row_dict[row[0]] = row[1]
    # return row_dict
    row_list = []
    for row_num in range(1, n_rows):
        row = table.row_values(row_num)
        row_list.append(row[0])
    print(row_list)
    return row_list

def import_unit_batch(request):
    data = excel_table_by_name()
    unit_list = []
    
    # area
    # for v in data:
    #     new_unit = Area(
    #         name= v,
    #     )
    #     unit_list.append(new_unit)
    # Area.objects.bulk_create(unit_list)

    # pc
    # equipment_type = EquipmentType.objects.get(pk=1)
    # for v in data:
    #     new_unit = Equipment(
    #         name= v,
    #         equipment_type=equipment_type,
    #     )
    #     unit_list.append(new_unit)
    # Equipment.objects.bulk_create(unit_list)

    # lcd
    equipment_type = EquipmentType.objects.get(pk=2)
    for v in data:
        new_unit = Equipment(
            name= v,
            equipment_type=equipment_type,
        )
        unit_list.append(new_unit)
    Equipment.objects.bulk_create(unit_list)


    # app_names = AppName.objects.filter(id__in=(12, 13))
    
    # for k, v in data.items():
    #     longitude_latitude = v.split(',')
    #     new_unit = Equipment(
    #         name=longitude_latitude[0],
    #         equipment_type=0,
    #     )
    #     unit_list.append(new_unit)
    # Equipment.objects.bulk_create(unit_list)