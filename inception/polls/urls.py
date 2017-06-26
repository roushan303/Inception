from django.conf.urls import url
from polls import views

app_name = 'polls'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^question_input/$', views.enter_question, name='question_input'),
    url(r'^choice_input/$',views.enter_choice, name='choice_input'),
]