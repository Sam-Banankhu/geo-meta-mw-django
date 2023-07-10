from django.shortcuts import render
from django.http import JsonResponse
from .models import Region, District, City
import csv

def get_regions(request):
    regions = Region.objects.all()
    result = [{'id': r.id, 'name': r.name, 'code': r.code} for r in regions]
    return JsonResponse(result, safe=False)

def get_districts(request):
    districts = District.objects.all()
    result = [{'id': d.id, 'name': d.name, 'code': d.code, 'region': d.region.name} for d in districts]
    return JsonResponse(result, safe=False)

def get_district_by_code(request, code):
    try:
        district = District.objects.get(code=code.upper())
        district_data = {
            'id': district.id,
            'name': district.name,
            'code': district.code,
            'region': district.region.name
        }
        return JsonResponse(district_data)
    except District.DoesNotExist:
        return JsonResponse({'error': 'District not found'}, status=404)

def get_cities(request):
    cities = City.objects.all()
    result = [{'id': c.id, 'name': c.name, 'district': c.district.name, 'region': c.district.region.name} for c in cities]
    return JsonResponse(result, safe=False)

# code to download CSV of cities
def download_cities_csv(request):
    cities = City.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="cities.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['id', 'name', 'district_id'])  # CSV header
    
    for city in cities:
        writer.writerow([city.id, city.name, city.district_id])  # CSV data rows
    
    return response

def get_city_by_name(request, city_name):
    try:
        city = City.objects.get(name=city_name)
        city_data = {
            'id': city.id,
            'name': city.name,
            'region': city.district.region.name
        }
        return JsonResponse(city_data)
    except City.DoesNotExist:
        return JsonResponse({'error': 'City not found'}, status=404)

def get_cities_in_district(request, code):
    try:
        district = District.objects.get(code=code.upper())
        cities = City.objects.filter(district=district)
        city_data = [{'id': c.id, 'name': c.name, 'district_name': district.name} for c in cities]
        return JsonResponse(city_data, safe=False)
    except District.DoesNotExist:
        return JsonResponse({'error': 'District not found'}, status=404)

def get_zip_codes(request, city_name):
    try:
        city = City.objects.get(name=city_name)
        zip_codes = [v.zip_code for w in city.wards for v in w.villages]
        return JsonResponse({'city': city_name, 'zip_codes': zip_codes})
    except City.DoesNotExist:
        return JsonResponse({'error': 'City not found'}, status=404)
