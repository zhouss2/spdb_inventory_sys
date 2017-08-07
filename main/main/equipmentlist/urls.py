from django.conf.urls import url

from . import views
from main.equipmentlist.views import EquipmentListView, OperationListView

urlpatterns = [
    url(r'^$', EquipmentListView.as_view(), name='equipmentlist'),
    url(r'^operationlist/$', OperationListView.as_view(), name='operationlist'),
    # url(r'^ask/$', views.ask, name='ask'),
    # url(r'^all/$', views.all_question, name='all'),
    # url(r'^answered/$', views.answered, name='answered'),
    # url(r'^unanswered/$', views.unanswered, name='unanswered'),
    # url(r'^favorite/$', views.favorite, name='favorite'),
    # url(r'^answer/$', views.answer, name='answer'),
    # url(r'^answer/accept/$', views.accept, name='accept'),
    # url(r'^answer/vote/$', views.vote, name='vote'),
]
