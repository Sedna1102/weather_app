import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from datetime import datetime, timedelta
from io import BytesIO

# 🔐 Directly embedded API key (for personal use only)
API_KEY = "39701159c3ab0a00dce28e210f95886d"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            result_label.config(text=f"Error: {data.get('message')}")
            icon_label.config(image="")
            return

        city_name = data["name"]
        temp = data["main"]["temp"]
        condition = data["weather"][0]["main"]
        icon_code = data["weather"][0]["icon"]
        timezone_offset = data["timezone"]
        utc_time = datetime.utcnow()
        local_time = utc_time + timedelta(seconds=timezone_offset)
        formatted_time = local_time.strftime("%A, %d %B %Y\n%I:%M %p")

        result = (
            f"📍 City: {city_name}\n"
            f"🌡️ Temperature: {temp}°C\n"
            f"🌥️ Condition: {condition}\n"
            f"🕒 Local Time:\n{formatted_time}"
        )
        result_label.config(text=result)

        # Fetch and display weather icon
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        icon_img = Image.open(BytesIO(icon_response.content))
        icon_photo = ImageTk.PhotoImage(icon_img)
        icon_label.config(image=icon_photo)
        icon_label.image = icon_photo

    except Exception as e:
        result_label.config(text="Failed to retrieve weather data.")
        icon_label.config(image="")

# UI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.configure(bg="#f0f4f7")

tk.Label(root, text="Enter City Name:", font=("Helvetica", 12), bg="#f0f4f7").pack(pady=10)
city_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
city_entry.pack(pady=5)

search_button = tk.Button(root, text="Search Weather", font=("Helvetica", 12), command=get_weather, bg="#4a90e2", fg="white")
search_button.pack(pady=10)

icon_label = tk.Label(root, bg="#f0f4f7")
icon_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f4f7", justify="left")
result_label.pack(pady=15)

root.mainloop()
