
from django.urls import path 

from . import views

urlpatterns = [
    path('sightings/',views.sightings),
    path('<int:unique_squirrel_id>/', views.sightings_details),
    path('add_sightings/',views.sightings_add),
 ]
