from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.equipments, name='equipments'),
    url(r'^import_unit_batch/$', views.import_unit_batch, name='import_unit_batch'),


    # url(r'^ask/$', views.ask, name='ask'),
    # url(r'^all/$', views.all_question, name='all'),
    # url(r'^answered/$', views.answered, name='answered'),
    # url(r'^unanswered/$', views.unanswered, name='unanswered'),
    # url(r'^favorite/$', views.favorite, name='favorite'),
    # url(r'^answer/$', views.answer, name='answer'),
    # url(r'^answer/accept/$', views.accept, name='accept'),
    # url(r'^answer/vote/$', views.vote, name='vote'),
    # url(r'^equipmentlist/$', EquipmentListView.as_view(), name='equipment-list'),
]
