from collections import defaultdict
import json

# Transform area data into desired format
with open("postleitzahlen.geojson") as f:
    plz_data = json.load(f)
plz_lookup = {}
for area in plz_data['features']:
    curr_plz = area['properties']['postcode']
    plz_lookup[curr_plz] = area


city_to_plzs = defaultdict(list)
for area in plz_data['features']:
    curr_city_name = area['properties']['locality'].lower()
    city_to_plzs[curr_city_name].append(area['properties']['postcode'])