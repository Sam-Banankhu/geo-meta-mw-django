import os
import csv
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metamw.settings')
django.setup()

from api.models import Region, District, City

def populate_data():
    # Populate regions
    regions_csv_path = os.path.join(os.getcwd(), 'data', 'regions.csv')
    with open(regions_csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            region = Region(name=row['name'], code=row['code'])
            region.save()

    # Populate districts
    districts_csv_path = os.path.join(os.getcwd(), 'data', 'districts.csv')
    with open(districts_csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            district = District(name=row['name'], code=row['code'], region_id=row['region'])

            district.save()

    # Populate cities
    cities_csv_path = os.path.join(os.getcwd(), 'data', 'cities.csv')
    with open(cities_csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city = City(name=row['name'], district_id=row['district_id'])

            city.save()

# Call the function to populate the data
populate_data()
