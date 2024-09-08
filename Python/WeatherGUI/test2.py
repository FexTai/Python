import customtkinter
from translate import Translator
import requests
from PIL import Image
import os
import pygame

pygame.init()
music_faz = "fweddy.mp3.mp3"

def play_music():
    pygame.mixer.music.load(music_faz)
    pygame.mixer.music.play()

# helpVar
hv = 0
hv2 = 0

# main window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("600x800")
root.resizable(False, False)

root.title("Wettervorhersage")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Icon Collection
search_icon = customtkinter.CTkImage(dark_image=Image.open("search.png"))

cloudy_icon = os.path.join(os.path.dirname(__file__), "cloudy.png")
img1 = customtkinter.CTkImage(light_image=Image.open(cloudy_icon), size=(110, 110))

cold_icon = os.path.join(os.path.dirname(__file__), "cold.png")
img2 = customtkinter.CTkImage(light_image=Image.open(cold_icon), size=(40, 40))

hot_icon = os.path.join(os.path.dirname(__file__), "hot.png")
img3 = customtkinter.CTkImage(light_image=Image.open(hot_icon), size=(40, 40))

parsunny_icon = os.path.join(os.path.dirname(__file__), "partially sunny.png")
img4 = customtkinter.CTkImage(light_image=Image.open(parsunny_icon), size=(110, 110))

rainy_icon = os.path.join(os.path.dirname(__file__), "rainy.png")
img5 = customtkinter.CTkImage(light_image=Image.open(rainy_icon), size=(110, 110))

snowy_icon = os.path.join(os.path.dirname(__file__), "snowy.png")
img6 = customtkinter.CTkImage(light_image=Image.open(snowy_icon), size=(110, 110))

sunny_icon = os.path.join(os.path.dirname(__file__), "sunny.png")
img7 = customtkinter.CTkImage(light_image=Image.open(sunny_icon), size=(110, 110))

thunder_icon = os.path.join(os.path.dirname(__file__), "thunder.png")
img8 = customtkinter.CTkImage(light_image=Image.open(thunder_icon), size=(110, 110))

wind_icon = os.path.join(os.path.dirname(__file__), "wind1.png")
img9 = customtkinter.CTkImage(light_image=Image.open(wind_icon), size=(40, 40))

tmzone_icon = os.path.join(os.path.dirname(__file__), "timezone.png")
img0 = customtkinter.CTkImage(light_image=Image.open(tmzone_icon), size=(43, 43))

humidity_icon = os.path.join(os.path.dirname(__file__), "humidity.png")
img11 = customtkinter.CTkImage(light_image=Image.open(humidity_icon), size=(40, 40))

clarity_icon = os.path.join(os.path.dirname(__file__), "clar.png")
img12 = customtkinter.CTkImage(light_image=Image.open(clarity_icon), size=(40, 40))

haze_icon = os.path.join(os.path.dirname(__file__), "haze.png")
img13 = customtkinter.CTkImage(light_image=Image.open(haze_icon), size=(110, 110))

drizzle_icon = os.path.join(os.path.dirname(__file__), "drizzle.png")
img14 = customtkinter.CTkImage(light_image=Image.open(drizzle_icon), size=(110, 110))

foggy_icon = os.path.join(os.path.dirname(__file__), "foggy.png")
img15 = customtkinter.CTkImage(light_image=Image.open(foggy_icon), size=(110, 110))

# Openweather API key
api_key = "d355490244cb91be451de6d43bf1c4b3"

url = ""
weather_data = []


# Funktionen

def click():
    global url, weather_data, city, hv, hv2, labs1, labs2
    label.place_forget()
    label1.place_forget()
    labs1.place_forget()
    labs2.place_forget()
    hf = city.get()
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + hf + "&APPID=" + api_key
    weather_data = requests.get(url).json()
    try:
        if hf == "amogus":
            labs2.place(x=150, y=130)
            label.place_forget()
            label1.place_forget()
        elif hf == "fassbier":
            labs1.place(x=0, y=130)
            label.place_forget()
            label1.place_forget()
            play_music()
        if weather_data["message"] == "city not found":
            label.place(x=140, y=50)
            label1.place(x=220, y=70)
    except:
        translator = Translator(to_lang="de")
        eng_weatherinfo = str(weather_data["weather"][0]["description"])
        zone = weather_data["timezone"]
        utc = abs(zone // 3600)
        if zone > 0:
            hv = "+"
        elif zone < 0:
            hv = "-"
        # Navigieren durch die Datenbank von weather_data
        print(weather_data)

        # Wetter icons auswählen
        if weather_data["weather"][0]["main"] == "Clear":
            label_weathericon.configure(image=img7)
        elif weather_data["weather"][0]["main"] == "Haze":
            label_weathericon.configure(image=img13)
        elif weather_data["weather"][0]["main"] == "Clouds":
            if weather_data["weather"][0]["description"] == "overcast clouds":
                label_weathericon.configure(image=img1)
            else:
                label_weathericon.configure(image=img4)
        elif weather_data["weather"][0]["main"] == "Rain":
            label_weathericon.configure(image=img1)
        elif weather_data["weather"][0]["main"] == "Drizzle":
            label_weathericon.configure(image=img14)
        elif weather_data["weather"][0]["main"] == "Snow":
            label_weathericon.configure(image=img6)
        elif weather_data["weather"][0]["main"] == "Thunderstorm":
            label_weathericon.configure(image=img8)
        elif weather_data["weather"][0]["main"] == "Fog" or weather_data["weather"][0]["main"] == "Mist":
            label_weathericon.configure(image=img15)

        # Wetterdaten einblenden
        labelct.configure(text=str(weather_data["name"]) + ", " + str(weather_data["sys"]["country"]))
        labelct.pack(padx=0, pady=70)

        # Temperatur
        labelt.configure(text=str(round((weather_data["main"]["temp"]) - 275.15, 1)) + "°")
        labelt.place(x=55, y=130)

        # gefühlte Temperatur
        labelfk.configure(text="gefühlt " + str(round((weather_data["main"]["feels_like"]) - 275.15, 1)) + "°")
        labelfk.place(x=55, y=200)

        # Tiefsttemperatur
        labeltf.configure(text=str(round((weather_data["main"]["temp_min"]) - 275.15, 1)) + "°")
        labeltf.place(x=95, y=365)
        label_cold.place(x=50, y=355)

        # Windgeschwindigkeit
        label_speed.configure(text=str(weather_data["wind"]["speed"]) + "m/s")
        label_speed.place(x=305, y=320)
        label_wind.place(x=260, y=310)

        # Höchsttemperatur
        labelht.configure(text=str(round((weather_data["main"]["temp_max"]) - 275.15, 1)) + "°")
        labelht.place(x=95, y=320)
        label_hot.place(x=50, y=310)

        # Zeitzone
        label.tmz.configure(text="UTC" + hv + str(utc))
        label_tmz.place(x=257, y=355)
        label.tmz.place(x=305, y=365)

        # Luftfeuchtigkeit
        label_hum.configure(text=str(weather_data["main"]["humidity"]) + "%")
        label_hum.place(x=97, y=410)
        label_hicon.place(x=50, y=400)

        # Sichtweite
        label_cl.configure(text=str(weather_data["visibility"]) + "m")
        label_cl.place(x=305, y=410)
        label_clicon.place(x=260, y=400)

        # Wettericon
        label_weathericon.place(x=270, y=130)

        # Wetterbeschreibung
        label_weatherinfo.configure(text=str(translator.translate(eng_weatherinfo)))
        label_weatherinfo.place(relx=0.985, rely=0.35, anchor="e")


def change():
    global f1, f2
    f1 = customtkinter.CTkCheckBox(root, offvalue=0, onvalue=1, text="Dark mode").place(x=0, y=0)
    f2 = customtkinter.CTkCheckBox(root, offvalue=2, onvalue=3, text="Ligt mode").place(x=0, y=25)


# Buttons
suche = customtkinter.CTkButton(root, width=30, height=30, text=" ", image=search_icon, command=click,
                                hover_color="cyan").place(x=350, y=25)

opt = customtkinter.CTkButton(root, width=30, height=30, text="///", command=change).pack()

# Text labels
city = customtkinter.StringVar()
city1 = customtkinter.CTkEntry(master=root, textvariable=city, font=("Arial", 18))
city1.place(x=210, y=25)

label = customtkinter.CTkLabel(frame, text="Leider nichts gefunden!", font=("Arial", 20))  # Nichts gefunden
label1 = customtkinter.CTkLabel(frame, text="☹", font=("", 50))

labelct = customtkinter.CTkLabel(frame, text="", font=("Arial", 30))

labelt = customtkinter.CTkLabel(frame, text="", font=("Arial", 50))

labelfk = customtkinter.CTkLabel(frame, text="", font=("Arial", 18))

labeltf = customtkinter.CTkLabel(frame, text="", font=("Arial", 20))

labelht = customtkinter.CTkLabel(frame, text="", font=("Arial", 20))

label_speed = customtkinter.CTkLabel(frame, text="", font=("Arial", 20))

label.tmz = customtkinter.CTkLabel(frame, text="", font=("Arial", 20))

label_hum = customtkinter.CTkLabel(frame, text="", font=("Arial", 20))

label_cl = customtkinter.CTkLabel(frame, text="", font=("Arial", 20))

label_weatherdesc = customtkinter.CTkLabel(frame, text="", font=("Arial", 20))

label_weatherinfo = customtkinter.CTkLabel(frame, text="", font=("Arial", 20), width=300, height=20)

f1 = customtkinter.CTkCheckBox(root, offvalue=0, onvalue=1, text="Dark mode")

f2 = customtkinter.CTkCheckBox(root, offvalue=2, onvalue=3, text="Ligt mode")

# Icon labels
label_weather = customtkinter.CTkLabel(frame, image="", text="")

label_hot = customtkinter.CTkLabel(frame, image=img3, text="")

label_cold = customtkinter.CTkLabel(frame, image=img2, text="")

label_wind = customtkinter.CTkLabel(frame, image=img9, text="")

label_tmz = customtkinter.CTkLabel(frame, image=img0, text="")

label_hicon = customtkinter.CTkLabel(frame, image=img11, text="")

label_clicon = customtkinter.CTkLabel(frame, image=img12, text="")

label_weathericon = customtkinter.CTkLabel(frame, image=img1, text="")

# easter eggs
labs1 = customtkinter.CTkLabel(frame, text="OH MY GUD GUYZ, IZ THIS FWEDDY FASSBIER???", font=("Arial", 20))
labs2 = customtkinter.CTkLabel(frame, text="GAMEMASTER?!=??", font=("Arial", 20))

root.mainloop()
