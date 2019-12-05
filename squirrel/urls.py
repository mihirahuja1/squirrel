
from django.urls import path 

from . import views

urlpatterns = [
    path('sightings/', views.sightings),
    path('sightings/add/', views.sightings_add, name='add'),
    path('sightings/stats/', views.sightings_stats),
    path('sightings/<unique_squirrel_id>/', views.sightings_edit, name='edit'),
    path('map/',views.map),
 ]
