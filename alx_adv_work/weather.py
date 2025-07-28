import requests

API_KEY = "99b9c71ce73d4a49a15223925252607"
BASE_URL = "https://api.weatherapi.com/v1/"

city_name = input(f"Enter the right location (e.g. lagos, accra): ")


url = f"{BASE_URL}current.json?key={API_KEY}&q={city_name}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    location = data['location']["name"]
    country = data['location']["country"]
    tempt = data["current"]["temp_c"]
    conditions = data["current"]["condition"]["text"]
    windy = data["current"]["wind_mph"]
    humid = data["current"]["humidity"]

    print(f"\nCurrent Weather in {location}, {country} ")
    print(f"Current Temperature in {location} is {tempt}°C")
    print(f"Current Wind/mph in {location} is {windy}mph")
    print(f"Current Humidity in {location} is {humid}")
else: 
    print("Failed to retrieve weather data. Check city name or API key.")