from translate import Translator
import requests
import sys

gertrans = Translator(to_lang="eng")

hv = 0

api_key = "d355490244cb91be451de6d43bf1c4b3"
city = input("Gib deine Stadt/Land an: ")
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" + api_key

weather_data = requests.get(url).json()
print(weather_data)

try:
    if weather_data["message"] == "city not found":
        print()
        print("Stadt nicht gefunden!")
    sys.exit()
except:
    print()
    # Navigieren durch die Datenbank von weather_data
    temperature = str(round((weather_data["main"]["temp"]) - 275.15, 1)) + "℃"
    fltemperature = str(round((weather_data["main"]["feels_like"]) - 275.15, 1)) + "℃"
    hoechst = str(round((weather_data["main"]["temp_max"]) - 275.15, 1)) + "℃"
    tiefst = str(round((weather_data["main"]["temp_min"]) - 275.15, 1)) + "℃"
    luftfeu = str(weather_data["main"]["humidity"]) + "%"
    druck = str(weather_data["main"]["pressure"]) + "hPa"
    zone = weather_data["timezone"]
    utc = abs(zone // 3600)
    if zone > 0:
        hv = "+"
    elif zone < 0:
        hv = "-"
    sicht = str(weather_data["visibility"]) + "m"
    wind = str(weather_data["wind"]["speed"]) + "m/s"
    name = str(weather_data["name"])
    try:
        country = str(weather_data["sys"]["country"])
    except:
        country = ""
    englische_wetterbeschreibung = str(weather_data["weather"][0]["description"])

    # Übersetzung der englischen Wetterbeschreibung ins Deutsche
    translator = Translator(to_lang="de")
    deutsche_wetterbeschreibung = translator.translate(englische_wetterbeschreibung)

    print(
        name, country, "\n",
        "Gefühlt:", fltemperature, "\n",
        "Temperatur:", temperature, "\n",
        "Höchsttemperatur:", hoechst, "\n",
        "Tiefsttemperatur:", tiefst, "\n",
        "Zeitzone:", f"UTC{hv}{utc}", "\n",
        "Sichtweite:", sicht, "\n",
        "Windgeschwindigkeit:", wind, "oder", str(round(weather_data["wind"]["speed"] * 3.6)) + "km/h" "\n",
        "Wetterbeschreibung:", deutsche_wetterbeschreibung, "\n")
