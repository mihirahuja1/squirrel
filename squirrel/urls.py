
from django.urls import path 

from . import views

urlpatterns = [
    path('', views.sightings, name='sightings'),
    path('<int:unique_squirrel_id>/', views.sightings_details),
    path('sightings/add/',views.sightings_add),
    path('map/',views.map),
 ]
