import requests

city = input("Sisesta soovitud linn: ")
api_key = "8a5423c830f1401083fd32af05d01cef"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    #print(f"Ilma kirjeldus: {weather}")
    print(f"Hetke temperatuur: {city} {temperature} °C")
else:
    print("Viga andmete allalaadimisel:", response.status_code)
