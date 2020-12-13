from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_event', views.addEvent),
    path('delete_event', views.deleteEvent),
    path('edit_event', views.editEvent),
    path('update_event', views.updateEvent),
    path('search_event', views.searchEvent),
    path('share_event', views.shareEvent),
    path('signup/', views.signup),
]
