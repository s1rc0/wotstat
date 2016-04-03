from django.conf.urls import url

from . import views

app_name = 'stats'
urlpatterns = [
    url(r'^$', views.index, name='index'), # ex: /stats/
    url(r'^(?P<account_id>[0-9]+)/$', views.detail, name='detail'), # ex: /stats/5/
    url(r'^(?P<account_id>[0-9]+)/results/$', views.results, name='results'), # ex: /stats/5/results/
    url(r'^(?P<account_id>[0-9]+)/vote/$', views.vote, name='vote'), # ex: /stats/5/vote/
]