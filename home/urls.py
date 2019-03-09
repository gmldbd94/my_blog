from django.urls import path
from . import views
appname = 'home'

urlpatterns = [
    path('', views.index, name='index'),

]
