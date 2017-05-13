from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main, name='main'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^intro/$', views.intro, name='intro'),
	url(r'^intro_task/$', views.intro_task, name='intro_task'),
	url(r'^notice/$', views.notice, name='notice'),
	url(r'^qna/$', views.qna, name='qna'),
	url(r'^login/$', views.login, name='login'),
	url(r'^login/$', views.login, name='logout'),
]