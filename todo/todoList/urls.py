from django.conf.urls import url

from . import views


app_name = 'todoList'
urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^(?P<todo_id>[0-9]+)/$', views.editieren, name='editieren'),
               url(r'^(?P<todo_id>[0-9]+)/change/$', views.change, name='change'),
               url(r'^(?P<todo_id>[0-9]+)/create/$', views.create, name='create'),
               ]
