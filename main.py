import requests

def hava_durumu(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=tr"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Hava durumu verilerini çekme
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        print(f"Hava Durumu Bilgileri - {city_name}:")
        print(f"Sıcaklık: {temp} °C")
        print(f"Nem: {humidity}%")
        print(f"Açıklama: {description}")
        print(f"Rüzgar Hızı: {wind_speed} m/s")
    else:
        print("Hava durumu verileri alınamadı.")



sehir = input("Hava durumu bilgisini almak istediğiniz şehri girin: ")
api_anahtari = "c4481a7bc3487eb3e857e43cd712308a"
hava_durumu(sehir, api_anahtari)
