from django.urls import path
from . import views

app_name = 'bloggers'

urlpatterns = [
    path('', views.home, name='home'),
    path('bloggers_list/', views.blogger_list, name='bloggers_list'),  # список блогерів
    path('blogger/<int:id>/', views.blogger_detail, name='blogger_detail'),  # деталі блогера
    path('news/', views.blogger_news, name='news'),  # сторінка новин
]
