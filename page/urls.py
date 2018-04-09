from django.conf.urls import url
from page import views

urlpatterns = [
    #url(r'^(?P<id>\d+)?(\/)?$', views.index, name='index'),
    url(r'^(?:(?P<id>\d+)/)?$', views.index, name='index'),
    url(r'^player/(?P<id>\d+)/$', views.player, name='players')
]

# url(r'^(?:\?id=(?P<id>\d+))?$')
# url(r'^players/\?id=(?P<id>\d+)$')
# url(r'^(?:(?P<id>\d+)/)?$')
# url(r'^players/(?P<id>\d+)/$')