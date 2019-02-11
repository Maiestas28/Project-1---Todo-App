from django.conf.urls import url

from . import views
app_name = 'todoapp'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='index'),
    #todoapp/1
    url(r'^(?P<task_id>[0-9]+)/$', views.DetailView.as_view(),name='detail'),
]
