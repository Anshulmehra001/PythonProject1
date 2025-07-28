import requests

# Input from user
city = input('Enter the name of the city\n')

# WeatherAPI URL with your API key
api_key = '132298e0197544ac837190738250806'
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

# Make the GET request
r = requests.get(url)

# Check if the response was successful (status code 200)
if r.status_code == 200:
    data = r.json()
    # Parse the data to get desired information
    city_name = data['location']['name']
    region = data['location']['region']
    country = data['location']['country']
    temperature = data['current']['temp_c']
    weather_description = data['current']['condition']['text']

    print(f"Weather in {city_name}, {region}, {country}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {weather_description}")
else:
    print(f"Error: Could not fetch data for {city}. Please check the city name and try again.")




