import customtkinter
from PIL import Image
import requests
import os

# optional translator
try:
    from translate import Translator
    _translator = Translator(to_lang="de")
    def translate_text(s):
        try:
            return _translator.translate(s)
        except Exception:
            return s
except Exception:
    _translator = None
    def translate_text(s):
        return s

# Konfiguration
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("600x800")
root.resizable(False, False)
root.title("Wettervorhersage")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Basisverzeichnis für Bilder (Verzeichnis der aktuellen Datei)
base_dir = os.path.dirname(__file__)

# Hilfsfunktion: CTkImage sicher laden
def load_ctkimage(fname, size=None):
    path = os.path.join(base_dir, fname)
    if not os.path.isfile(path):
        print(f"[WARN] Bild nicht gefunden: {path}")
        return None
    try:
        pil = Image.open(path)
        if size:
            return customtkinter.CTkImage(light_image=pil, size=size)
        return customtkinter.CTkImage(light_image=pil)
    except Exception as e:
        print(f"[WARN] Fehler beim Laden von {path}: {e}")
        return None

# Icons
search_icon = load_ctkimage("SH.png", size=(24, 24))
img_cloudy = load_ctkimage("cloudy.png", size=(110, 110))
img_cold = load_ctkimage("cold.png", size=(40, 40))
img_hot = load_ctkimage("hot.png", size=(40, 40))
img_partly = load_ctkimage("partially sunny.png", size=(110, 110))
img_rainy = load_ctkimage("rainy.png", size=(110, 110))
img_snow = load_ctkimage("snowy.png", size=(110, 110))
img_sunny = load_ctkimage("sunny.png", size=(110, 110))
img_thunder = load_ctkimage("thunder.png", size=(110, 110))
img_wind = load_ctkimage("wind1.png", size=(40, 40))
img_tmz = load_ctkimage("timezone.png", size=(43, 43))
img_hum = load_ctkimage("humidity.png", size=(40, 40))
img_cl = load_ctkimage("clar.png", size=(40, 40))
img_haze = load_ctkimage("haze.png", size=(110, 110))
img_drizzle = load_ctkimage("drizzle.png", size=(110, 110))
img_fog = load_ctkimage("foggy.png", size=(110, 110))

# OpenWeather API key
api_key = "d355490244cb91be451de6d43bf1c4b3"

# Hilfsfunktion: Formatiere Zeitzone (z.B. UTC+5:30)
def format_timezone(seconds_offset):
    sign = "+" if seconds_offset >= 0 else "-"
    seconds = abs(int(seconds_offset))
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    if minutes == 0:
        return f"UTC{sign}{hours}"
    return f"UTC{sign}{hours}:{minutes:02d}"

# --- Widgets ---
city_var = customtkinter.StringVar()
entry_city = customtkinter.CTkEntry(master=root, textvariable=city_var, font=("Arial", 18))
entry_city.place(x=210, y=25)

# Labels (erzeugt, aber noch nicht platziert)
label_notfound = customtkinter.CTkLabel(frame, text="Leider nichts gefunden!", font=("Arial", 20))
label_sad = customtkinter.CTkLabel(frame, text="☹", font=("", 50))

label_citycountry = customtkinter.CTkLabel(frame, text="", font=("Arial", 30))
label_temp = customtkinter.CTkLabel(frame, text="", font=("Arial", 50))
label_feels = customtkinter.CTkLabel(frame, text="", font=("Arial", 18))
label_temp_min = customtkinter.CTkLabel(frame, text="", font=("Arial", 20))
label_temp_max = customtkinter.CTkLabel(frame, text="", font=("Arial", 20))
label_wind = customtkinter.CTkLabel(frame, text="", font=("Arial", 20))
label_tz = customtkinter.CTkLabel(frame, text="", font=("Arial", 20))
label_humidity = customtkinter.CTkLabel(frame, text="", font=("Arial", 20))
label_visibility = customtkinter.CTkLabel(frame, text="", font=("Arial", 20))
label_weatherinfo = customtkinter.CTkLabel(frame, text="", font=("Arial", 20), width=300, height=20)
label_weathericon = customtkinter.CTkLabel(frame, image=img_cloudy, text="")

# kleine Icon-Labels
label_icon_hot = customtkinter.CTkLabel(frame, image=img_hot, text="")
label_icon_cold = customtkinter.CTkLabel(frame, image=img_cold, text="")
label_icon_wind = customtkinter.CTkLabel(frame, image=img_wind, text="")
label_icon_tz = customtkinter.CTkLabel(frame, image=img_tmz, text="")
label_icon_hum = customtkinter.CTkLabel(frame, image=img_hum, text="")
label_icon_vis = customtkinter.CTkLabel(frame, image=img_cl, text="")

# Theme-Auswahlmenü
def change_appearance(choice):
    mapping = {"Dunkel": "dark", "Hell": "light", "System": "system"}
    mode = mapping.get(choice, choice.lower())
    try:
        customtkinter.set_appearance_mode(mode)
    except Exception as e:
        print("Fehler beim Wechseln des Themes:", e)

# CTkOptionMenu erlaubt direkte Auswahl von Dunkel/Hell/System
theme_menu = customtkinter.CTkOptionMenu(root, values=["Dunkel", "Hell", "System"], command=change_appearance)
# Default passend zur initialen Einstellung oben
theme_menu.set("Dunkel")
theme_menu.place(x=10, y=5)

# Button 
btn_search = customtkinter.CTkButton(root, width=30, height=30, text=" ", image=search_icon, hover_color="cyan")
btn_search.place(x=350, y=25)



def click():
    city_name = city_var.get().strip()
    # vorherige Anzeige zurücksetzen
    for w in (label_notfound, label_sad, label_citycountry, label_temp, label_feels,
              label_temp_min, label_temp_max, label_wind, label_tz, label_humidity,
              label_visibility, label_weatherinfo, label_weathericon):
        try:
            w.place_forget()
            w.pack_forget()
        except Exception:
            pass

    if not city_name:
        label_notfound.configure(text="Bitte Stadt eingeben")
        label_notfound.place(x=140, y=50)
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={api_key}"
    try:
        resp = requests.get(url, timeout=8)
        data = resp.json()
    except Exception as e:
        label_notfound.configure(text="Fehler bei der Netzwerkverbindung")
        label_notfound.place(x=140, y=50)
        print("Request-Fehler:", e)
        return

    # Fehlerbehandlung der API-Antwort
    if resp.status_code != 200 or data.get("cod") != 200:
        msg = data.get("message", "Stadt nicht gefunden")
        label_notfound.configure(text=f"{msg}")
        label_sad.place(x=220, y=70)
        label_notfound.place(x=140, y=50)
        return

    # Übersetze Wetterbeschreibung (Fallback möglich)
    eng_weatherinfo = str(data["weather"][0]["description"]) if data.get("weather") else ""
    translated = translate_text(eng_weatherinfo)

    # Wähle Icon nach Hauptwetter
    main = data["weather"][0]["main"] if data.get("weather") else ""
    desc = data["weather"][0]["description"] if data.get("weather") else ""

    if main == "Clear":
        img = img_sunny
    elif main == "Haze":
        img = img_haze
    elif main == "Clouds":
        img = img_cloudy if desc == "overcast clouds" else img_partly
    elif main == "Rain":
        img = img_rainy
    elif main == "Drizzle":
        img = img_drizzle
    elif main == "Snow":
        img = img_snow
    elif main == "Thunderstorm":
        img = img_thunder
    elif main in ("Fog", "Mist"):
        img = img_fog
    else:
        img = img_cloudy

    if img is not None:
        label_weathericon.configure(image=img)

    # Stadt, Land
    label_citycountry.configure(text=f"{data.get('name','')} , {data.get('sys',{}).get('country','')}")
    label_citycountry.pack(padx=0, pady=70)

    # Temperaturen: Kelvin -> Celsius (korrekt: -273.15)
    try:
        temp = data['main']['temp'] - 273.15
        feels = data['main']['feels_like'] - 273.15
        tmin = data['main']['temp_min'] - 273.15
        tmax = data['main']['temp_max'] - 273.15

        label_temp.configure(text=f"{round(temp,1)}°")
        label_temp.place(x=55, y=130)

        label_feels.configure(text=f"gefühlt {round(feels,1)}°")
        label_feels.place(x=55, y=200)

        label_temp_min.configure(text=f"{round(tmin,1)}°")
        label_temp_min.place(x=95, y=365)
        label_icon_cold.place(x=50, y=355)

        label_temp_max.configure(text=f"{round(tmax,1)}°")
        label_temp_max.place(x=95, y=320)
        label_icon_hot.place(x=50, y=310)
    except Exception as e:
        print("Temperatur-Daten fehlen:", e)

    # Wind
    try:
        wind_speed = data.get('wind', {}).get('speed', '')
        label_wind.configure(text=f"{wind_speed} m/s")
        label_wind.place(x=305, y=320)
        label_icon_wind.place(x=260, y=310)
    except Exception as e:
        print("Wind-Daten fehlen:", e)

    # Zeitzone
    try:
        tz_seconds = data.get('timezone', 0)
        tz_str = format_timezone(tz_seconds)
        label_tz.configure(text=tz_str)
        label_tz.place(x=305, y=365)
        label_icon_tz.place(x=257, y=355)
    except Exception as e:
        print("Zeitzone Fehler:", e)

    # Luftfeuchtigkeit
    try:
        humidity = data['main']['humidity']
        label_humidity.configure(text=f"{humidity}%")
        label_humidity.place(x=97, y=410)
        label_icon_hum.place(x=50, y=400)
    except Exception as e:
        print("Humidity fehlt:", e)

    # Sichtweite
    try:
        visibility = data.get('visibility', '')
        label_visibility.configure(text=f"{visibility} m")
        label_visibility.place(x=305, y=410)
        label_icon_vis.place(x=260, y=400)
    except Exception as e:
        print("Visibility fehlt:", e)

    # Wetterbeschreibung
    label_weatherinfo.configure(text=translated)
    label_weatherinfo.place(relx=0.985, rely=0.35, anchor="e")

    # Icon platzieren
    label_weathericon.place(x=270, y=130)


# Verbinde Button mit Funktion
btn_search.configure(command=click)

# mainloop
root.mainloop()
