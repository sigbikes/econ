from django.conf.urls import url
from c_growth import views

urlpatterns= [
    url(r'^$', views.index, name = 'index'),
    url(r'^index/', views.index, name = 'index'),
    url(r'^about/', views.about, name = 'about'),


]
