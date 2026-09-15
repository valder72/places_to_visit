from django.urls import path, include
from . import views

app_name = 'places_to_visit'

urlpatterns = [
    path('', views.base, name='home'),
    path('add/', views.add_place, name='add_place'),
    path('<int:num>/', views.place_info, name='place_detail'),
    path('list/', views.list_places, name="places_list")
]
