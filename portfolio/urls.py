from django.urls import path
from django.conf.urls import url
from portfolio import views


urlpatterns = [
    path('', views.index, name='index'),
]