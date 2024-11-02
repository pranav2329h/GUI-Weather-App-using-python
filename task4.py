import requests

def get_weather(city):
    api_key = "82636c4c0b62c492db28b3dc8873db96"  
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric' 
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  

        data = response.json()
        
        if data.get("cod") != 200:
            print(f"Error: {data.get('message', 'Unable to retrieve data')}")
            return
        
        main = data['main']
        weather = data['weather'][0]
        
        print(f"\nWeather in {city.capitalize()}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Description: {weather['description'].capitalize()}")
    
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

if __name__ == "__main__":
    while True:
        city = input("Enter city name (or type 'quit' to exit): ")
        if city.lower() == 'quit':
            print("Exiting the weather app.")
            break
        get_weather(city)