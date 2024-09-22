import requests
import pandas as pd

def fetch_nearby_attractions(lat, lon):
    # Replace with your preferred OSM API endpoint for attractions
    url = f"https://overpass-api.de/api/interpreter?data=[out:json];(node[\"tourism\"=\"attraction\"]({lat - 0.05},{lon - 0.05},{lat + 0.05},{lon + 0.05}););out;"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        attractions = []
        for element in data['elements']:
            attractions.append({
                'name': element.get('tags', {}).get('name', 'Unknown'),
                'lat': element['lat'],
                'lon': element['lon']
            })
        return pd.DataFrame(attractions)
    else:
        print("Error fetching attractions")
        return pd.DataFrame(columns=['name', 'lat', 'lon'])

def get_attractions_for_hotel(hotel_data):
    lat, lon = hotel_data['lat'], hotel_data['lng']
    attractions_df = fetch_nearby_attractions(lat, lon)
    return attractions_df
