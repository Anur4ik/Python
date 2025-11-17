from django.urls import path, re_path
from . import views

app_name = 'bloggers'

urlpatterns = [
    path('', views.home, name='home'),
    path('bloggers/', views.blogger_list, name='bloggers_list'),
    path('news/', views.blogger_news, name='news'),
    path('bloggers/i_am/', views.i_am, name='top_bloggers'),
    re_path(r'^bloggers/(?P<slug>[-a-zA-Z0-9_]+)/$', views.blogger_detail, name='blogger_detail' ),
]
