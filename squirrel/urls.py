
from django.urls import path 

from . import views

urlpatterns = [
    path('sightings/', views.sightings),
    path('sightings/<int:unique_squirrel_id>/', views.sightings_details, name='edit'),
    path('sightings/add/',views.sightings_add, name='add'),
    path('map/',views.map),
 ]
