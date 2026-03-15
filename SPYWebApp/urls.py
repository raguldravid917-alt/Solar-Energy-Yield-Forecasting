from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wform', views.wform, name='wform'),
    path('dform', views.dform, name='dform'),
]