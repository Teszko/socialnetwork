from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'todoList'
urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^change/(?P<todo_id>[0-9]+)$', views.editieren, name='editieren'),
               url(r'^create/$', views.erstellen, name='erstellen'),
               url(r'^impressum/$', views.impressum, name='impressum'),
               url(r'^save/$', views.save, name='save'),
               url(r'^save/(?P<todo_id>[0-9]+)$', views.save, name='save'),
               url(r'^delete/(?P<todo_id>[0-9]+)$', views.delete, name='delete'),
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
