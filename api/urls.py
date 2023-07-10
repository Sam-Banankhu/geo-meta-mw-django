from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('regions', views.get_regions, name='regions'),
    path('districts', views.get_districts, name='districts'),
    path('districts/<str:code>', views.get_district_by_code, name='district_by_code'),
    path('cities', views.get_cities, name='cities'),
    path('cities/download', views.download_cities_csv, name='download_cities_csv'),
    path('city/<str:city_name>', views.get_city_by_name, name='city_by_name'),
    path('districts/<str:code>/cities', views.get_cities_in_district, name='cities_in_district'),
    path('cities/<str:city_name>/zip-codes', views.get_zip_codes, name='zip_codes'),
]
