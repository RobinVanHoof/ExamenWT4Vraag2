from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.voegToe, name='voegToe'),
    url(r'^sortbycalorie/$', views.sortbycalorie, name="sortbycalorie"),
    url(r'^sortbynaam/$', views.sortbynaam, name="sortbynaam")
]
