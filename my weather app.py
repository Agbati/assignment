import requests

city_name="Accra"


API_key="7b33bc7a8ef8e73bf9d2a1a42d7304b9"

the_weather  =  requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}")


weather_condition=the_weather.json()
print(weather_condition)

temperature = weather_condition ["main"]["temp"]

if temperature  <= 300.38:
    print(f"The weather is warm ")

elif temperature <= 373.15:
    print(f"the weather is hot")

else:
    print(f"no weather  changes here")
