from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^home$', views.home, name='home'),
	url(r'^editor$', views.editor, name='editor'),
	url(r'^(?P<s_id>\d+)/StoryPage/$', views.StoryPage, name='StoryPage'),

]