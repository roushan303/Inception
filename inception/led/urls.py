from django.conf.urls import url
from led import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    ]