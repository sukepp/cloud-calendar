from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_event', views.addEvent),
    path('signup/', views.signup),
]
