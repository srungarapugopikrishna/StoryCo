from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^home$', views.home, name='home'),
	url(r'^editor$', views.editor, name='editor'),
	url(r'^(?P<s_id>.*)/editor_child/$', views.editor_child, name='editorChild'	),
	url(r'^some_view$', views.some_view, name='some_view'),
	url(r'^(?P<s_id>.*)/StoryPage/$', views.StoryPage, name='StoryPage'),
	url(r'^(?P<s_id>.*)/visualize/$', views.visualize, name='visualize'	),
	url(r'^get_data$', views.get_data, name='get_data'),
]