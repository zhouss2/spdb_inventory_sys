from django.conf.urls import url

from . import views
from main.equipmentlist.views import EquipmentListView, OperationListView,equipmentareaidles, equipmentlistbyarea, equipmentlistbylcd,equipmentlistbypc
urlpatterns = [
    url(r'^$', EquipmentListView.as_view(), name='equipmentlist'),
    url(r'^operationlist/$', OperationListView.as_view(), name='operationlist'),
    url(r'^equipmentareaidle/$', equipmentareaidles, name='equipmentareaidles'),
    url(r'^equipmentlistbylcd/$', equipmentlistbylcd, name='equipmentlistbylcd'),
    url(r'^equipmentlistbyarea/$', equipmentlistbyarea, name='equipmentlistbyarea'),
    url(r'^equipmentlistbypc/$', equipmentlistbypc, name='equipmentlistbypc'),
    # url(r'^ask/$', views.ask, name='ask'),
    # url(r'^ask/$', views.ask, name='ask'),
    # url(r'^all/$', views.all_question, name='all'),
    # url(r'^answered/$', views.answered, name='answered'),
    # url(r'^unanswered/$', views.unanswered, name='unanswered'),
    # url(r'^favorite/$', views.favorite, name='favorite'),
    # url(r'^answer/$', views.answer, name='answer'),
    # url(r'^answer/accept/$', views.accept, name='accept'),
    # url(r'^answer/vote/$', views.vote, name='vote'),
]
