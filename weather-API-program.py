import requests
from pprint import pprint as pp
import datetime
import time

# Create a free OpenWeather API account where you will get the API key to allow access to the weather data required

appid = "Your API key"  # Replace with your OpenWeather API Key


# Function to get weather data
def get_weather(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={appid}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Could not retrieve weather data.")
        return None

    data = response.json()

    # Extract relevant data
    weather_info = {
        "city": data["name"],
        "temperature": round(data["main"]["temp"], 1),
        "description": data["weather"][0]["description"][:20] + "..." if len(data["weather"][0]["description"]) > 20 else data["weather"][0]["description"],  # String Slicing
        "humidity": data["main"]["humidity"],
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    return weather_info

# Function to suggest clothing based on temperature
def recommend_outfit(temp):
    if temp < 10:
        return "Wear a heavy jacket and a scarf. ❄️"
    elif temp < 20:
        return "A light jacket should be enough. 🍂"
    else:
        return "Shorts and a t-shirt are fine! ☀️"


# Linking user input, weather data, and outfit suggestion
def ask_user():
    while True:  # While Loop - Keep asking for cities until user exits
        city_name = input("\nEnter a city (or type 'exit' to quit): ").strip()

        if city_name.lower() == "exit":
            print("Exiting the weather app. Have a great day! 😊")
            break  # Exit the loop

        weather = get_weather(city_name)

        if weather:

            print(f"\nWeather in {weather['city']} 🌍")
            print(f"Temperature: {weather['temperature']}°C 🌡️")
            print(f"Condition: {weather['description']}")
            print(f"Humidity: {weather['humidity']}% 💧")
            print(f"Time: {weather['time']} ⏳")

        # Call the outfit suggestion function
        outfit = recommend_outfit(weather["temperature"])
        print(f"\nRecommended Outfit: {outfit}")

    with open("weather_log.txt", "a") as file: # allowing the file to be appended
        file.write(f"{weather['time']} - {weather['city']}: {weather['temperature']}°C, {weather['description']}\n")

    print("\n(Weather log updated!)")

# Run the program
ask_user()