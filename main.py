import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        temp = str(data["main"]["temp"]).split('.')
        temp = temp[0]
        real_temp = str(data["main"]["feels_like"]).split('.')
        real_temp = real_temp[0]

        print(f"✋Погода в городе: {city}\n🌡{temp}°C ({real_temp}°C), {wd}\n"
                             f"💦Влажность: {humidity}%\n💨Ветер: {wind} м/с\n"
                             f"❗️Данные на: {datetime.datetime.now().strftime('%d.%m %H:%M')}\n"
                             f"Хорошего дня!"
                             )

    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = str(input("Введите название города: "))
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()