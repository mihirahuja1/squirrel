
from django.urls import path 

from . import views

urlpatterns = [
    path('sightings/', views.sightings),
    path('sightings/<unique_squirrel_id>/', views.sightings_edit, name='edit'),
    path('sightings/add/',views.sightings_add, name='add'),
    path('map/',views.map),
 ]
