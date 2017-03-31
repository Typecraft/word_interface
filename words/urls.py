from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^word$', views.word, name='word'),
    url(r'^home$', views.home, name='home'),
    url(r'^my-words$', views.my_words, name='mywords'),
]
