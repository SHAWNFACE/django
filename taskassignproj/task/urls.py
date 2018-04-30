from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$',views.login,name='login'),
    url(r'^loginform/$',views.myloginform),
    url(r'^logout/$',auth_views.logout,name='logout'),
    url(r'^admininsert/$',views.admininsert,name='admininsert'),
]

