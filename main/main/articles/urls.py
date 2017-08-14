from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.articles, name='articles'),
    url(r'^write/$', views.write, name='write'),
    url(r'^preview/$', views.preview, name='preview'),
    url(r'^drafts/$', views.drafts, name='drafts'),
    url(r'^comment/$', views.comment, name='comment'),
    url(r'^tag/(?P<tag_name>.+)/$', views.tag, name='tag'),
    url(r'^edit/(?P<article_id>\d+)/$', views.edit, name='edit_article'),
    url(r'^(?P<slug>[-\w]+)/$', views.article, name='article'),
    # url(r'^media/uploads/', views.big_file_download, name='big_file_download'),
    # url(r'^upload/', views.upload),
    url(r'^uploads/(?P<year>\d+)/(?P<filename>\S+)$', views.download_file, name='download_file'),
]
