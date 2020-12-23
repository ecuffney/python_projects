
import requests

API_ROOT = 'https://www.metaweather.com'
API_LOCATION = '/api/location/search/?query='
API_WEATHER = '/api/location/'  # + woeid

def fetch_location(query):
    return requests.get(API_ROOT + API_LOCATION + query).json()

def fetch_weather(woeid):
    return requests.get(API_ROOT + API_WEATHER + str(woeid)).json()

def disambiguate_locations(locations):
    print("Ambiguous location! Did you mean:")
    for loc in locations:
        print(f"\t* {loc['title']}")

def display_weather(weather):
    print(f"Weather for {weather['title']}:")
    for entry in weather['consolidated_weather']:
        date = entry['applicable_date']
        high = entry['max_temp']
        low = entry['min_temp']
        state = entry['weather_state_name']
        print(f"{date}\t{state}\thigh {high:2.1f}°C\tlow {low:2.1f}°C")

def weather_dialog():
    try:
        where = ''
        while not where:
            where = input("Where in the world are you? ")
        locations = fetch_location(where)
        if len(locations) == 0:
            print("I don't know where that is. Please be more specific:")
        elif len(locations) > 1:
            disambiguate_locations(locations)
        else:
            woeid = locations[0]['woeid']
            display_weather(fetch_weather(woeid))
    except requests.exceptions.ConnectionError:
        print("Couldn't connect to server! Is the network up?")

if __name__ == '__main__':
    while True:
        weather_dialog()
