from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^editor$', views.editor, name='editor'),
    url(r'^(?P<s_id>.*)/editor_child/$', views.editor_child, name='editorChild'),
    url(r'^(?P<s_id>.*)/StoryPage/$', views.StoryPage, name='StoryPage'),
    url(r'^(?P<s_id>.*)/visualize/$', views.visualize, name='visualize'),
    url(r'^get_data$', views.get_data, name='get_data'),
    url(r'^genreList$', views.genreList, name='genreList'),
    url(r'^item$', views.item, name='item'),
    url(r'^episode$', views.first_episode(), name='episode'),
    url(r'^items$', views.items_list, name='items_list'),
    url(r'^(?P<item_id>.*)/item_details/$', views.item_details, name='item_details'),
]
